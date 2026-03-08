from git_scan import scan_repo
from tasks import debug_code, build_project


class Tools:

    def scan_repository(self, repo_path):
        return scan_repo(repo_path)

    def run_tests(self, repo_path):
        return debug_code(repo_path)

    def build_project(self, repo_path):
        return build_project(repo_path)