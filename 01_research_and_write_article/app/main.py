from fastapi import FastAPI
from crewai import Crew

from app.agents import planner, writer, editor
from app.tasks import plan, write, edit

app = FastAPI(
    title="Research and write article CrewAI",
    version="0.0.1",
    )

crew = Crew(
    agents=[planner, writer, editor],
    tasks=[plan, write, edit],
    verbose=2
)

@app.get("/")
def read_root():
    return {"Hello": "Crew AI"}

@app.post("/crew/write-article")
def write_article(topic: str):
    result = crew.kickoff(inputs={"topic": topic})    
    return {"article": result}