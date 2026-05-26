import asyncio
import os
import sys

# Ensure backend can be imported
sys.path.append(os.getcwd())

from backend.app.agents.brain import brain_agent
from backend.app.agents.sage import sage_agent

async def test_synthesis():
    query = "What is the essence of Dharma?"
    print(f"Testing synthesis for query: {query}")

    # Simulate Brain consultation
    thought = await brain_agent.consult_brain(query)
    print("\n[BRAIN THOUGHT]")
    print(f"Synthesis: {thought['synthesis'][:100]}...")
    print(f"Themes: {thought['themes']}")
    print(f"Fragments Found: {len(thought['all_fragments'])}")

    # Simulate Sage formatting
    response = await sage_agent.format_wisdom(thought)
    print("\n[SAGE RESPONSE]")
    print(f"Reflection: {response.reflection}")
    print(f"Meaning: {response.meaning}")
    print(f"Sources: {len(response.sources)}")

    if len(response.sources) > 0:
        print(f"First Source Score: {response.sources[0].get('score')}")

if __name__ == "__main__":
    asyncio.run(test_synthesis())
