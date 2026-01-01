import yaml
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.google import Gemini

db = SqliteDb(db_file="memories/insults.db")

with open("config.yaml","r") as f:
    CONFIG = yaml.safe_load(f)

agent = Agent(
    name="Agent A",
    role="The Insulter",
    model=Gemini(id="gemini-2.5-flash-lite",temperature=0.91),
    db=db,
    enable_user_memories=True,
    instructions=CONFIG['instructions_for_a'],

)

agent.print_response("do you have something to say about agent B?")