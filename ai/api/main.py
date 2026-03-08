from fastapi import FastAPI
from pydantic import BaseModel

from agent import DevAgent

app = FastAPI()

agent = DevAgent()


class GoalRequest(BaseModel):
    repo_path: str
    goal: str


@app.post("/agent")
def run_agent(req: GoalRequest):

    result = agent.execute_goal(req.repo_path, req.goal)

    return result