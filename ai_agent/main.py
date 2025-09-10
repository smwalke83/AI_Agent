import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_ITERS

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)
    if not args:
        print('Usage: uv run main.py "your prompt here"')
        sys.exit(1)
    prompt = " ".join(args)
    if verbose:
        print("User prompt:", prompt)
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)
        try:
            response, function_responses = generate_content(client, messages, verbose)
            if len(response.candidates) > 0:
                for candidate in response.candidates:
                    messages.append(candidate.content)
            if len(function_responses) > 0:
                messages.append(types.Content(role = "user", parts = function_responses))
            if not response.function_calls and response.text:
                break
        except Exception as e:
            print(f"Exception: {e}")
            messages.append(types.Content(role = "user", parts = [types.Part(text = f"Error: {e}")]))

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model = "gemini-2.0-flash-001",
        contents = messages,
        config = types.GenerateContentConfig(
            tools = [available_functions], system_instruction = system_prompt
        ),
    )
    function_responses = []
    if verbose:
        if response.function_calls:
            for function_call in response.function_calls:
                result = call_function(function_call, verbose = True)
                if not result.parts[0].function_response.response:
                    raise Exception("Empty function call result")
                resp = result.parts[0].function_response.response
                print(f"-> {resp.get('result')}")
                function_responses.append(result.parts[0])
            if not function_responses:
                raise Exception("No function responses generated")
        else:
            print("Prompt tokens:", response.usage_metadata.prompt_token_count)
            print("Response tokens:", response.usage_metadata.candidates_token_count)
            print(response.text)
    else:
        if response.function_calls:
            for function_call in response.function_calls:
                result = call_function(function_call)
                if not result.parts[0].function_response.response:
                    raise Exception("Empty function call result")
                function_responses.append(result.parts[0])
            if not function_responses:
                raise Exception("No function responses generated")
        else:
            print(response.text)
    return response, function_responses


if __name__ == "__main__":
    main()
