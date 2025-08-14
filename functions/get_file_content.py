import os
from config import Config
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the content of a specified file, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to retrieve content from, relative to the working directory.",
            ),
        },
    ),
)


def get_file_content(working_directory, file_path):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))
    # check if the full_path is inside the working_directory
    if working_directory not in full_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # check if the directory is a directory
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        content = ''
        with open(full_path, 'r') as file:
            content = file.read()

        char_limit = Config.GET_FILE_CONTENT_CHAR_LIMIT

        if len(content) > char_limit:
            content = content[:char_limit]
            content += f'\n\n[...File "{file_path}" truncated at {char_limit} characters]'
        return content
    except Exception as e:
        return f'Error: {str(e)}'
