import requests

from planner import Planner
from tools import Tools
from memory import Memory
from loop import AgentLoop

OLLAMA_URL = "http://localhost:11434/api/generate"


class DevAgent:

    def __init__(self):

        self.planner = Planner()
        self.tools = Tools()
        self.memory = Memory()
        self.loop = AgentLoop()

    def ask_llm(self, prompt):

        payload = {
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }

        r = requests.post(OLLAMA_URL, json=payload)

        return r.json()["response"]
        
    def autonomous_fix(self, repo_path, error):

        return self.loop.run(repo_path, error)

    def execute_goal(self, repo_path, goal):

        """
        エージェント実行
        """

        plan = self.planner.create_plan(goal)

        results = []

        for step in plan:

            if step == "scan_repository":
                result = self.tools.scan_repository(repo_path)

            elif step == "run_tests":
                result = self.tools.run_tests(repo_path)

            elif step == "build_project":
                result = self.tools.build_project(repo_path)

            elif step == "generate_docs":

                files = self.tools.scan_repository(repo_path)

                prompt = f"""
                このプロジェクトのREADME.mdを生成

                Files:
                {files}
                """

                result = self.ask_llm(prompt)

            else:
                result = "unknown step"

            self.memory.add({step: result})
            results.append(result)

        return {
            "plan": plan,
            "results": results
        }