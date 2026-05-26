from app.core.retrieval import retrieval_service
from app.core.knowledge_graph import knowledge_graph
from app.agents.seeker import seeker_agent
from app.services.brain_store import brain_store
from app.services.llm_service import llm_service
from app.services.context_merger import context_merger
from app.services.theme_extractor import theme_extractor
from app.core.observability import obs
import hashlib

class BrainAgent:
    """
    The Brain Agent acts as the central intelligence of the Ramayana AI.
    It synthesizes retrieved context into cohesive mythological insights.
    """
    def __init__(self):
        self.memory_cache = {}

    async def learn_from_context(self, fragments: list, query: str = ""):
        """
        Synthesizes sacred fragments into a singular vision using real LLM logic.
        """
        if not fragments:
            return "Seeking clarity in the void...", []

        # 1. Merge Context
        merged_context = context_merger.merge(fragments)

        # 2. LLM Synthesis
        prompt = f"""
        Given the following sacred fragments related to '{query}', synthesize a coherent
        explanation that captures the philosophical and narrative essence.

        {merged_context}

        Synthesis:
        """
        base_synthesis = await llm_service.generate(prompt, system_prompt="You are the synthesis engine of the Ramayana AI.")

        # 3. Extract Themes
        themes = await theme_extractor.extract_themes(base_synthesis)

        # 4. Dialectical Refinement: Brain asks Seeker to challenge this synthesis
        challenge = await seeker_agent.pose_challenge(base_synthesis, query)

        # 5. Final Refinement (Simplified for Phase 1.5)
        refined_synthesis = f"{base_synthesis}\n\n[Dialectical Resolution]: {challenge}"

        # Store in BrainStore
        brain_store.store_wisdom(query, {
            "base_synthesis": base_synthesis,
            "challenge": challenge,
            "refined_synthesis": refined_synthesis,
            "themes": themes,
            "fragments": fragments
        })

        return refined_synthesis, themes

    @obs.trace_agent("BrainAgent")
    async def consult_brain(self, query: str):
        """
        Coordinates the retrieval and synthesis process.
        """
        # 1. Check BrainStore first for pre-refined wisdom
        stored = brain_store.get_wisdom(query)
        if stored:
             return {
                "query": query,
                "synthesis": stored['refined_synthesis'],
                "wisdom_nugget": "Established wisdom from the collective memory.",
                "all_fragments": stored.get('fragments', []),
                "connections": [],
                "themes": stored.get('themes', []),
                "certainty": 1.0
            }

        # 2. Retrieve raw context
        enriched_fragments = retrieval_service.retrieve_context(query, limit=5)
        obs.log_retrieval(query, enriched_fragments)

        # 3. Synthesize
        synthesis_note, themes = await self.learn_from_context(enriched_fragments, query=query)

        # 4. Knowledge Graph relations
        relations = await knowledge_graph.get_relations(query)

        # 5. Final Thought synthesis
        obs.log_synthesis("Brain", query, synthesis_note)

        thought = {
            "query": query,
            "synthesis": synthesis_note,
            "wisdom_nugget": enriched_fragments[0]['content'] if enriched_fragments else "Silence is the first teacher.",
            "all_fragments": enriched_fragments,
            "connections": relations,
            "themes": themes,
            "certainty": 0.85 if enriched_fragments else 0.1
        }

        return thought

brain_agent = BrainAgent()
