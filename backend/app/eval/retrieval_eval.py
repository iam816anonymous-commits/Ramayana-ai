import asyncio
import json
import os
import sys

sys.path.append(os.getcwd())

from backend.app.core.retrieval import retrieval_service

async def run_retrieval_eval():
    with open("backend/app/eval/dataset.json", "r") as f:
        dataset = json.load(f)

    total = len(dataset)
    hits = 0

    print(f"Running Retrieval Evaluation on {total} samples...")

    for item in dataset:
        query = item["query"]
        expected_keywords = item["expected_keywords"]

        results = retrieval_service.retrieve_context(query, limit=5)

        # Check if any of the top 5 results contain expected keywords
        found = False
        for res in results:
            content = res["content"].lower()
            if any(kw.lower() in content for kw in expected_keywords):
                found = True
                break

        if found:
            hits += 1
            print(f" [PASS] Query: {query}")
        else:
            print(f" [FAIL] Query: {query} (No keywords {expected_keywords} found in top 5)")

    accuracy = (hits / total) * 100
    print(f"\nRetrieval Accuracy (Recall@5): {accuracy:.2f}%")

if __name__ == "__main__":
    asyncio.run(run_retrieval_eval())
