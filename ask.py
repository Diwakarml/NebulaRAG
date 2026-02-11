import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8002")

def ask_question(query_text: str):
    try:
        resp = requests.post(
            f"{API_BASE_URL}/query",
            json={"query": query_text, "top_k": 3},
            timeout=60
        )
        resp.raise_for_status()
        data = resp.json()
        print("\n" + "="*50)
        print(f"AI ANSWER ({data.get('llm_provider', 'unknown')}):")
        print("-" * 50)
        print(data.get("answer"))
        print("="*50 + "\n")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Welcome to your Free RAG Assistant!")
    print(f"Connected to: {API_BASE_URL}")
    print("Type 'exit' to quit.\n")
    
    while True:
        query = input("Ask a complex question: ")
        if query.lower() in ["exit", "quit"]:
            break
        if not query.strip():
            continue
        
        print("Thinking...")
        ask_question(query)

if __name__ == "__main__":
    main()
