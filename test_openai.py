import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print(f"Using API Key: {api_key[:10]}...{api_key[-10:]}")
else:
    print("API Key not found!")

client = OpenAI(api_key=api_key)

try:
    resp = client.embeddings.create(model="text-embedding-3-small", input="Hello world")
    print("Success! Embedding created.")
    print(f"Dimension: {len(resp.data[0].embedding)}")
except Exception as e:
    print(f"Failed: {e}")
