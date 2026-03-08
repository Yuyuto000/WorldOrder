# APIサーバー
from fastapi import FastAPI
from pydantic import BaseModel

from agent import DevAgent

app = FastAPI()
agent = DevAgent()

class RepoRequest(BaseModel):
    repo_path: str

class TaskRequest(BaseModel):
    repo_path: str
    task: str


@app.post("/scan_repo")
def scan_repo(req: RepoRequest):
    """
    Gitリポジトリ解析
    """
    result = agent.scan_repository(req.repo_path)
    return {"result": result}


@app.post("/run_task")
def run_task(req: TaskRequest):
    """
    エージェントタスク実行
    """
    result = agent.run_task(req.repo_path, req.task)
    return {"result": result}


@app.post("/generate_docs")
def generate_docs(req: RepoRequest):
    """
    Docs生成
    """
    result = agent.generate_docs(req.repo_path)
    return {"result": result}