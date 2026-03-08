from fastapi import FastAPI
from pydantic import BaseModel

from agent import DevAgent

app = FastAPI()

agent = DevAgent()


class GoalRequest(BaseModel):
    repo_path: str
    goal: str

class FixRequest(BaseModel):
    repo_path: str
    error: str


@app.post("/auto_fix")
def auto_fix(req: FixRequest):

    result = agent.autonomous_fix(req.repo_path, req.error)

    return result
    
@app.post("/agent")
def run_agent(req: GoalRequest):

    result = agent.execute_goal(req.repo_path, req.goal)

    return result