# Gitリポジトリ解析

import os


def scan_repo(repo_path):

    result = []

    for root, dirs, files in os.walk(repo_path):

        for f in files:

            if f.endswith(".py") or f.endswith(".java") or f.endswith(".js"):

                path = os.path.join(root, f)

                result.append(path)

    return result