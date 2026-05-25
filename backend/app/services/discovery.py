import asyncio
import logging
from app.core.vector_store import vector_db
from app.agents.brain import brain_agent
from app.services.brain_store import brain_store

logger = logging.getLogger(__name__)

class DiscoveryService:
    """
    The Discovery Service manages the autonomous 'learning' loop.
    It iterates through the vector store, picks chunks, and has the
    Brain and Seeker agents synthesize them into the BrainStore.
    """

    async def run_discovery_loop(self, limit: int = 20):
        """
        An autonomous loop where agents 'read' the data and ask each other questions.
        """
        logger.info(f"Starting discovery loop for {limit} items...")

        # 1. Fetch random/top items from the vector store
        # Since we don't have a 'scroll' or 'list' easily in our basic wrapper,
        # we'll use a zero vector search to get a spread of documents.
        try:
            # Most models use 384 dimensions for all-MiniLM-L6-v2
            zero_vector = [0.0] * 384
            results = vector_db.search(zero_vector, limit=limit)

            for point in results:
                text = point.payload.get("text", "")
                if not text:
                    continue

                # Derive a 'topic' or 'question' from the chunk for indexing
                # In a real system, we'd ask the Brain to 'Summarize this chunk into a query'
                # For Phase 1 discovery, we use the first 50 chars as a proxy topic.
                topic = text[:50].strip() + "..."

                logger.info(f"Agents discovering wisdom for: {topic}")

                # The Brain Agent handles the internal dialogue with the Seeker Agent
                # and stores the result in brain_store.json
                await brain_agent.learn_from_context([text], query=topic)

            logger.info("Discovery loop completed successfully.")
            return len(results)

        except Exception as e:
            logger.error(f"Discovery loop failed: {e}")
            return 0

discovery_service = DiscoveryService()
