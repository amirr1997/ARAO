# app/main.py

from fastapi import FastAPI
from app.agents.planner import PlannerAgent
from app.orchestrator import Orchestrator

app = FastAPI()

planner = PlannerAgent()

orchestrator = Orchestrator(
    planner=planner,
    analyst=lambda x: f"Analyzed: {x}",
    writer=lambda x: f"Report: {x}"
)

@app.post("/run")
def run(task: str):
    return orchestrator.run(task)