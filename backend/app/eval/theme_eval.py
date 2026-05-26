import asyncio
import json
import os
import sys

sys.path.append(os.getcwd())

from backend.app.agents.brain import brain_agent

async def run_theme_eval():
    with open("backend/app/eval/dataset.json", "r") as f:
        dataset = json.load(f)

    total = len(dataset)
    correct_themes = 0

    print(f"Running Theme Extraction Evaluation on {total} samples...")

    for item in dataset:
        query = item["query"]
        expected_themes = [t.lower() for t in item["expected_themes"]]

        thought = await brain_agent.consult_brain(query)
        extracted_themes = [t.lower() for t in thought["themes"]]

        # Check if any expected theme is in extracted themes
        match = any(et in extracted_themes for et in expected_themes)

        if match:
            correct_themes += 1
            print(f" [PASS] Query: {query} (Extracted: {extracted_themes})")
        else:
            print(f" [FAIL] Query: {query} (Expected: {expected_themes}, Extracted: {extracted_themes})")

    accuracy = (correct_themes / total) * 100
    print(f"\nTheme Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    asyncio.run(run_theme_eval())
