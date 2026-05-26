import time
import logging
from functools import wraps
from typing import Any, Dict, List
import json
import os

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ramayana_observability.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("RamayanaAI")

class Observability:
    """
    Simple observability helper for Phase 1.5.
    Tracks latency, query patterns, and retrieval quality logs.
    """

    @staticmethod
    def trace_agent(agent_name: str):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                start_time = time.time()
                logger.info(f"[AGENT_START] {agent_name} - Processing...")
                try:
                    result = func(*args, **kwargs)
                    duration = time.time() - start_time
                    logger.info(f"[AGENT_SUCCESS] {agent_name} - Duration: {duration:.2f}s")
                    return result
                except Exception as e:
                    duration = time.time() - start_time
                    logger.error(f"[AGENT_FAILURE] {agent_name} - Duration: {duration:.2f}s - Error: {str(e)}")
                    raise e
            return wrapper
        return decorator

    @staticmethod
    def log_retrieval(query: str, results: List[Dict[str, Any]]):
        avg_score = sum(r.get('score', 0) for r in results) / len(results) if results else 0
        logger.info(f"[RETRIEVAL] Query: '{query}' - Results: {len(results)} - Avg Score: {avg_score:.4f}")

    @staticmethod
    def log_synthesis(agent: str, query: str, response: str):
        # Log a snippet of synthesis for quality auditing
        snippet = response[:100].replace('\n', ' ') + "..."
        logger.info(f"[SYNTHESIS] Agent: {agent} - Query: '{query}' - Snippet: {snippet}")

obs = Observability()
