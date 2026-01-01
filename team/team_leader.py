import asyncio
from textwrap import dedent

from agno.agent import Agent
from agno.models.google import Gemini
from agno.team import Team
from agents.agent_a import agent_a 
from agents.agent_b import agent_b
import os


insult_team = Team(
    name="Insult Battle",
    model=Gemini(id="gemini-2.5-flash",temperature=0.91,api_key=os.getenv("GOOGLE_API_KEY")),
    members=[agent_a, agent_b],
    share_member_interactions=True,
    instructions=dedent("""
    You are the spectator of this converssation between Agent A and Agent B.

    RULES:
    1. Start asking agent A if they has something to anyone
    2. Pass Agent A's response to Agent B for their response
    3. Pass Agent B's response back to Agent A
    4. Continue alternating between agents

    ENDING CONDITIONS:
    - If ANY agent says "I'M DONE TALKING TO THIS PERSON" (or similar),
      immediately STOP the battle and ask them for their final justification.
    - Then summarize the battle and declare your verdict on who "won"
    - Maximum 10 rounds if no one quits

    Keep the conversation flowing naturally. After each response,
    immediately delegate to the other agent.
    You may add things to one's dialogues to others, to provoke others
    """),
    markdown=True,
    show_members_responses=True,
)



asyncio.run(
        insult_team.aprint_response(
            input="Ask A if they have something to say.",
            stream=True,
        )
    )
