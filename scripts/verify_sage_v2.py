import requests
import json
import time

def verify():
    # Use the Sanctum endpoint which uses the Sage/Brain flow
    url = "http://localhost:8000/api/sanctum/reflect"
    payload = {"query": "What is the importance of Dharma in the forest exile?"}

    print(f"Sending request to {url}...")
    try:
        response = requests.post(url, json=payload, timeout=15)
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print("\n--- SANCTUM RESPONSE (SAGE + BRAIN) ---")
            print(json.dumps(data, indent=2))

            # Check for enhanced synthesis
            synthesis = data.get("brain_synthesis", "")
            if "Dharma" in synthesis:
                print("\n✅ Brain synthesis correctly identified the theme: 'Dharma'.")
            else:
                print(f"\n⚠️ Brain synthesis did not explicitly mention 'Dharma' theme. Synthesis was: {synthesis}")

            reflection = data.get("reflection", "").lower()
            if "resonate" in reflection:
                 print("✅ Sage tone is updated to 'resonate'.")
            else:
                 print(f"⚠️ Sage tone not updated? Reflection was: {reflection}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Failed to connect: {e}")

if __name__ == "__main__":
    verify()
