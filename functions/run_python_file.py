import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in a specified working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT, 
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Arguments to pass to the Python script.",
                ),
                description="Arguments to pass to the Python script. Defaults to empty array if not provided - no need to ask user for arguments unless they specifically mention them.",
                default=[]
            ),
        },
        required=["file_path"]
    )
)


def run_python_file(working_directory, file_path, args=[]):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    if working_directory not in full_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # if file path does not exists
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'

    # if file is not ending with .py
    if not file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run(
            ['python', full_path] + args,
            capture_output=True,
            text=True,
            timeout=30,
        )

        # if process exited with a non-zero code
        if result.returncode != 0:
            return f"Process exited with code {result.returncode}"
        
        # if no output
        if not result.stdout and not result.stderr:
            return "No output produced."

        stdout = f"STDOUT: {result.stdout}"
        stderr = f"STDERR: {result.stderr}"

        return f"{stdout}\n{stderr}"
    except Exception as e:
        return f"Error: executing Python file: {e}"
