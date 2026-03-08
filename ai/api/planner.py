# タスク分解AI

class Planner:

    def create_plan(self, goal):

        """
        ゴールをタスクへ分解
        """

        if "debug" in goal:
            return [
                "scan_repository",
                "run_tests",
                "fix_errors"
            ]

        if "build" in goal:
            return [
                "scan_repository",
                "build_project"
            ]

        if "docs" in goal:
            return [
                "scan_repository",
                "generate_docs"
            ]

        return ["scan_repository"]