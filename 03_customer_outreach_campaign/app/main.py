from fastapi import FastAPI
from crewai import Crew

from app.agents import sales_rep_agent, lead_sales_rep_agent
from app.tasks import lead_profiling_task, personalized_outreach_task

app = FastAPI(
    title="Customer Outreach CrewAI",
    version="0.0.1",
    )

crew = Crew(
    agents=[sales_rep_agent, 
            lead_sales_rep_agent],
    
    tasks=[lead_profiling_task, 
           personalized_outreach_task],
	
    verbose=2,
	memory=True
)

@app.get("/")
def read_root():
    return {"Hello": "Crew AI"}

@app.post("/process_task")
def process_task(lead_name: str, industry: str, key_decision_maker: str, position: str, milestone: str):
    inputs = {
    "lead_name": lead_name,
    "industry": industry,
    "key_decision_maker": key_decision_maker,
    "position": position,
    "milestone": milestone
}
    result = crew.kickoff(inputs=inputs)

    return {"result": result}