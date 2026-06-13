# app/orchestrator.py

class Orchestrator:
    def __init__(self, planner, analyst, writer):
        self.planner = planner
        self.analyst = analyst
        self.writer = writer

    def run(self, task: str):

        plan = self.planner.run(task)

        analysis = self.analyst(task)
        report = self.writer(analysis)

        return {
            "plan": plan,
            "report": report
        }