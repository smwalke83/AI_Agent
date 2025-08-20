import os
import subprocess

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