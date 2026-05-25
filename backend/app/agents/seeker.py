import random

class SeekerAgent:
    """
    The Seeker Agent represents the inquisitive mind.
    It challenges the Brain Agent by asking 'Why' and 'What if',
    pushing the synthesis to a deeper level.
    """

    async def pose_challenge(self, context_summary: str, query: str):
        """
        Generates a deepening question based on the current synthesis.
        """
        challenges = [
            f"If {query} is true, how does it reconcile with the core tenet of Dharma?",
            f"What was the hidden emotional weight behind this event?",
            f"How would a different version of the Ramayana interpret this 'wisdom'?",
            f"Is there a contradiction between the actions taken and the ultimate goal?",
            f"What lesson does this hold for a seeker in the modern age?"
        ]

        # Pick a challenge that feels relevant or random for simulation
        selected = random.choice(challenges)
        return f"Challenge from the Seeker: {selected} (Based on: {context_summary[:50]}...)"

seeker_agent = SeekerAgent()
