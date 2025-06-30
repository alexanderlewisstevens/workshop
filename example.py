import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

client = OpenAI(api_key=api_key)

try:
    # Make a simple API call to list models (as a test)
    models = client.models.list()
    print("OpenAI API key is valid. Available models:")
    for model in models.data[:5]:  # Show first 5 models
        print("-", model.id)
except Exception as e:
    print("Failed to use OpenAI API:", e)
