# 開発タスク

import subprocess


def debug_code(repo_path):

    try:

        result = subprocess.run(
            ["pytest"],
            cwd=repo_path,
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:
        return str(e)


def build_project(repo_path):

    try:

        result = subprocess.run(
            ["python", "setup.py", "build"],
            cwd=repo_path,
            capture_output=True,
            text=True
        )

        return result.stdout

    except Exception as e:
        return str(e)