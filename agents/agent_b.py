import yaml
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.google import Gemini
import os
from dotenv import load_dotenv

load_dotenv("/workspaces/insults/.env")
db = SqliteDb(db_file="memories/insults.db")

with open("/workspaces/insults/agents/config.yaml","r") as f:
    CONFIG = yaml.safe_load(f)

agent_b = Agent(
    name="Agent B",
    role="The Dad Figure",
    model=Gemini(id="gemini-2.5-flash",temperature=0.91,api_key=os.getenv("GOOGLE_API_KEY")),
    db=db,
    enable_user_memories=True,
    instructions=CONFIG['instructions_for_b'],
    
    add_name_to_context=True

)

#agent.print_response("do you have something to say about agent A?")