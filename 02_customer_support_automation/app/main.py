from fastapi import FastAPI
from crewai import Crew

from app.agents import support_agent, support_quality_assurance_agent
from app.tasks import inquiry_resolution, quality_assurance_review


app = FastAPI(
    title="Customer Support Automation CrewAI",
    version="0.0.1",
    )

crew = Crew(
  agents=[support_agent, support_quality_assurance_agent],
  tasks=[inquiry_resolution, quality_assurance_review],
  verbose=2,
  memory=True
)

@app.get("/")
def read_root():
    return {"Hello": "Crew AI"}

@app.post("/inquiry_resolution")
def inquiry_resolution_endpoint(customer: str, person:str, inquiry: str):
    inputs = {
    "customer": customer,
    "person": person,
    "inquiry": inquiry
    }
    result = crew.kickoff(inputs=inputs)
    return {"result": result}