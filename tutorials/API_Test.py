import openai
import os  # Ensure os is imported

# Set the OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    # List available models to verify your API key
    response = openai.Model.list()
    print("Available models:")
    for model in response["data"]:
        print(f"- {model['id']}")
except Exception as e:
    print(f"Error: {e}")
