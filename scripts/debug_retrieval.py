import os
import sys

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), "backend"))

from app.core.retrieval import retrieval_service

def debug_search():
    query = "Who is Ravana?"
    print(f"Searching for: {query}")
    results = retrieval_service.retrieve_context(query, limit=5)
    for i, res in enumerate(results):
        print(f"\nResult {i+1} (Score: {res['score']}):")
        print(f"Content: {res['content'][:200]}...")
        print(f"Metadata: {res['metadata']}")

if __name__ == "__main__":
    debug_search()
