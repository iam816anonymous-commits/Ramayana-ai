import sys
import os

# Add the project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.app.core.retrieval import retrieval_service

def test():
    queries = [
        "Who is Rama's father?",
        "Where was Sita from?",
        "Why did Rama go to exile?"
    ]

    for query in queries:
        print(f"\nQuery: {query}")
        try:
            context = retrieval_service.retrieve_context(query)
            for i, chunk in enumerate(context):
                print(f"[{i+1}] {chunk[:100]}...")
        except Exception as e:
            print(f"Error retrieving context: {e}")

if __name__ == "__main__":
    test()
