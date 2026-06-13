class PlannerAgent:
    def run(self, task: str):
        return {
            "steps": [
                "research",
                "analyze",
                "write_report"
            ],
            "task": task
        }