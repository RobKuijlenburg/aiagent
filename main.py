import os
from dotenv import load_dotenv
from google import genai
from sys import argv, exit as sys_exit

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():
    args = argv
    print(args) 
    if len(args) != 2:
        print("Usage: python3 main.py '<your prompt here>'")
        sys_exit(1)
    prompt = args[1]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=prompt)
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
