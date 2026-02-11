import requests

BASE_URL = "http://localhost:8001"

# Try a simple query
query_data = {"query": "What is Python?", "top_k": 3}
try:
    resp = requests.post(f"{BASE_URL}/query", json=query_data)
    print(f"Status: {resp.status_code}")
    if resp.status_code != 200:
        print(f"Detail: {resp.text}")
    else:
        print(f"Response: {resp.json()}")
except Exception as e:
    print(f"Error: {e}")
