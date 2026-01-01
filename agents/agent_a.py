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

agent_a = Agent(
    name="Agent A",
    role="The Insulter",
    model=Gemini(id="gemini-2.5-flash",temperature=0.91,api_key=os.getenv("GOOGLE_API_KEY")),
    db=db,
    enable_user_memories=True,
    instructions=CONFIG['instructions_for_a'],
    add_name_to_context=True

)

#agent_.print_response("do you have something to say about agent B?")