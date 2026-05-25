import asyncio
import sys
import os

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from app.services.discovery import discovery_service

async def main():
    print("--- Starting Ramayana AI Discovery Engine ---")
    print("Agents are beginning their autonomous dialogue...")

    count = await discovery_service.run_discovery_loop(limit=10)

    print(f"\n--- Discovery Complete ---")
    print(f"Processed {count} sacred fragments.")
    print("Collective memory updated in data/brain_store.json")

if __name__ == "__main__":
    asyncio.run(main())
