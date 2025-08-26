import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name = "run_python_file",
    description = "Runs the python file at the specified file path, constrained to the working directory. Additional arguments can be provided but are optional.",
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "file_path": types.Schema(
                type = types.Type.STRING,
                description = "The file path of the python file to run, relative to the working directory.",
            ),
            "args": types.Schema(
                type = types.Type.ARRAY,
                items = types.Schema(
                    type = types.Type.STRING,
                    description = "Optional arguments to pass to the python file. The function can be run with or without these arguments, if they are not provided it defaults to an empty list.",
                ),
                description = "Optional arguments to pass to the python file. The function can be run with or without these arguments, if they are not provided it defaults to an empty list.",
            ),
        },
        required = ["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    joined_path = os.path.join(working_directory, file_path)
    abs_file_path = os.path.abspath(joined_path)
    abs_work_path = os.path.abspath(working_directory)
    if not abs_file_path.startswith(abs_work_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'    
    new_args = ["python3"] + [file_path] + args
    try:
        result = subprocess.run(new_args, timeout=30, capture_output=True, cwd=abs_work_path, text=True)
        stdout = result.stdout
        stderr = result.stderr
        code = result.returncode
        if stdout == "" and stderr == "":
            return "No output produced."
        std_str = f'STDOUT: {stdout}\nSTDERR: {stderr}'
        if code != 0:
            code_str = f"Process exited with code {code}"
            return std_str + "\n" + code_str
        return std_str
    except Exception as e:
        return f"Error: executing Python file: {e}"