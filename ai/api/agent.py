# AIエージェント

import requests

from git_scan import scan_repo
from tasks import debug_code, build_project

OLLAMA_URL = "http://localhost:11434/api/generate"


class DevAgent:

    def ask_llm(self, prompt):
        """
        LLMへ問い合わせ
        """
        payload = {
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }

        r = requests.post(OLLAMA_URL, json=payload)
        return r.json()["response"]

    def scan_repository(self, repo_path):
        """
        Gitリポジトリを解析
        """
        files = scan_repo(repo_path)

        prompt = f"""
        このGitリポジトリの構造を説明してください。

        Files:
        {files}
        """

        return self.ask_llm(prompt)

    def run_task(self, repo_path, task):

        if task == "debug":
            return debug_code(repo_path)

        if task == "build":
            return build_project(repo_path)

        return "unknown task"

    def generate_docs(self, repo_path):

        files = scan_repo(repo_path)

        prompt = f"""
        このプロジェクトのREADME.mdを生成してください

        Files:
        {files}

        必須
        - プロジェクト説明
        - API説明
        - TODO
        """

        return self.ask_llm(prompt)