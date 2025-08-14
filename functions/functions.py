from google.genai import types
from .get_file_content import get_file_content, schema_get_file_content
from .get_files_info import get_files_info, schema_get_files_info
from .run_python_file import run_python_file, schema_run_python_file
from .write_file import schema_write_file, write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_file_content,
        schema_get_files_info,
        schema_run_python_file,
        schema_write_file
    ]
)


def call_function(function_call_part: types.FunctionCall, verbose=False):
    if verbose:
        print(
            f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    function_name = str(function_call_part.name)
    args = function_call_part.args or {}

    working_directory = "calculator"
    args["working_directory"] = working_directory
    response = {}

    match function_name:
        case "get_file_content":
            response["result"] = get_file_content(**args)
        case "get_files_info":
            response["result"] = get_files_info(**args)
        case "run_python_file":
            response["result"] = run_python_file(**args)
        case "write_file":
            response["result"] = write_file(**args)
        case _:
            response['error'] = f"Unknown function: {function_name}"

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response=response
            )
        ]
    )
