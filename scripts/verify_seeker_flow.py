import requests
import json
import os
import time

def check():
    url = "http://localhost:8000/api/sanctum/reflect"
    query = "What is the essence of Hanuman's strength?"

    # Ensure a fresh state for this query if possible (though we don't have a reset API)
    # So we just run it and check for Seeker's involvement

    print(f"Asking: {query}")
    r = requests.post(url, json={"query": query})
    data = r.json()

    synthesis = data.get("brain_synthesis", "")
    print(f"Synthesis: {synthesis}")

    if "Challenge from the Seeker" in synthesis:
        print("✅ Seeker Agent challenged the Brain.")
    else:
        print("❌ Seeker Agent was NOT involved in the synthesis.")

    # Run again to check storage
    print("\nAsking same query again...")
    r = requests.post(url, json={"query": query})
    data = r.json()
    synthesis = data.get("brain_synthesis", "")
    print(f"Synthesis: {synthesis}")

    if "Retrieved from Eternal Memory" in synthesis:
        print("✅ Brain Store correctly retrieved established wisdom.")
    else:
        print("❌ Brain Store retrieval failed.")

if __name__ == "__main__":
    check()
