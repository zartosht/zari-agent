import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory="."):
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    # check if the full_path is inside the working_directory
    if working_directory not in full_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    # check if the directory is a directory
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    try:
        files = os.listdir(full_path)

        return "\n".join(
            [
                f" - {file}: file_size={os.path.getsize(os.path.join(full_path, file))} bytes, is_dir={os.path.isdir(os.path.join(full_path, file))}"
                for file in files
            ]
        )
    except Exception as e:
        return f'Error: {str(e)}'
