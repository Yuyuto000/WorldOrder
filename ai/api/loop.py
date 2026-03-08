import os

from code_parser import CodeParser
from patcher import Patcher
from reviewer import Reviewer


class AgentLoop:

    def __init__(self):

        self.parser = CodeParser()
        self.patcher = Patcher()
        self.reviewer = Reviewer()

    def fix_file(self, file_path, error):

        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()

        patched = self.patcher.generate_patch(file_path, code, error)

        review = self.reviewer.review(patched)

        if "OK" in review:

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(patched)

            return "patched"

        return "rejected"

    def run(self, repo_path, error):

        parsed = self.parser.parse_repo(repo_path)

        results = []

        for file in parsed:

            path = file["file"]

            result = self.fix_file(path, error)

            results.append({path: result})

        return results