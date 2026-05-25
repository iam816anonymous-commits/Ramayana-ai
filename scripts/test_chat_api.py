import httpx
import time

def test_chat():
    # Updated to match the backend router prefix
    url = "http://localhost:8000/api/characters/"
    payload = {
        "character": "Rama",
        "message": "Why did you accept the exile?"
    }

    # Wait a bit for server to start
    time.sleep(2)

    try:
        response = httpx.post(url, json=payload, timeout=10.0)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_chat()
