import ast
import os


class CodeParser:

    def parse_file(self, file_path):

        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())

        functions = []
        classes = []

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)

            if isinstance(node, ast.ClassDef):
                classes.append(node.name)

        return {
            "file": file_path,
            "functions": functions,
            "classes": classes
        }

    def parse_repo(self, repo_path):

        results = []

        for root, dirs, files in os.walk(repo_path):

            for f in files:

                if f.endswith(".py"):

                    path = os.path.join(root, f)

                    try:
                        results.append(self.parse_file(path))
                    except:
                        pass

        return results