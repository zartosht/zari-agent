import os
import sys
from google import genai
from config import Config
from google.genai import types
from dotenv import load_dotenv
from functions.functions import available_functions, call_function

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <content>")
        sys.exit(1)

    verbose = "--verbose" in sys.argv

    user_prompt = sys.argv[1]

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    for i in range(20):
        try:
            result = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    system_instruction=Config.SYSTEM_PROMPT,
                    tools=[available_functions]
                )
            )

            for candidate in result.candidates or []:
                if candidate.content is not None:
                    messages.append(candidate.content)

            for call in result.function_calls or []:
                call_result = call_function(call, verbose=verbose)
                if call_result.parts is None or call_result.parts[0].function_response is None:
                    raise Exception(
                        f"Function {call.name} failed"
                    )

                if verbose:
                    print(
                        f"-> {call_result.parts[0].function_response.response}")

                for part in call_result.parts:
                    if part.function_response is not None and part.function_response.response is not None:
                        if 'result' in part.function_response.response:
                            messages.append(types.Content(
                                role="user",
                                parts=[types.Part(
                                    text=part.function_response.response['result'])]
                            ))
                        if 'error' in part.function_response.response:
                            messages.append(types.Content(
                                role="user",
                                parts=[types.Part(
                                    text=part.function_response.response['error'])]
                            ))

            if verbose:
                print(f"User prompt: {user_prompt}")
                print("Prompt tokens:",
                      result.usage_metadata.prompt_token_count if result.usage_metadata else 0)
                print("Response tokens:",
                      result.usage_metadata.candidates_token_count if result.usage_metadata else 0)
                
            # Only treat as final response if there are no function calls to execute
            if result.function_calls and len(result.function_calls) > 0:
                # Skip accessing result.text when there are function calls to avoid warning
                continue
            elif result.text is not None:
                print("Final response:")
                print(result.text)
                break

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
