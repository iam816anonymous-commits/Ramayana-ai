import requests
import json

def check():
    base_url = "http://localhost:8000/api"

    # 1. Health
    print("Checking Backend Health...")
    r = requests.get(f"{base_url}/daily/health")
    print(f"Health: {r.status_code}")

    # 2. Timeline
    print("\nChecking Timeline API...")
    r = requests.get(f"{base_url}/timeline/")
    print(f"Timeline items: {len(r.json())}")

    # 3. Sanctum (Sage + Brain)
    print("\nChecking Sanctum (Sage + Brain)...")
    payload = {"query": "Tell me about Hanuman's devotion."}
    r = requests.post(f"{base_url}/sanctum/reflect", json=payload)
    data = r.json()
    print(f"Reflection: {data['reflection']}")
    print(f"Synthesis: {data['brain_synthesis']}")

    if "Bhakti" in data['brain_synthesis']:
        print("✅ Theme detection working correctly.")
    if "resonate" in data['reflection'].lower():
        print("✅ Sage tone working correctly.")

if __name__ == "__main__":
    check()
