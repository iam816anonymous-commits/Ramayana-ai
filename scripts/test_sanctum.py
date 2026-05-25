import httpx
import time

def test_sanctum():
    url = "http://localhost:8000/api/sanctum/reflect"
    payload = {
        "query": "What is the meaning of Rama's exile?"
    }

    time.sleep(5)

    try:
        response = httpx.post(url, json=payload, timeout=10.0)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_sanctum()
