from fastapi import FastAPI
from crewai import Crew 

from app.agents import venue_coordinator, logistics_manager, marketing_communications_agent
from app.tasks import venue_task, logistics_task, marketing_task

app = FastAPI(
    title="Automate Event Planning CrewAI",
    version="0.0.1",
    )

# Define the crew with agents and tasks
event_management_crew = Crew(
    agents=[venue_coordinator, 
            logistics_manager, 
            marketing_communications_agent],
    
    tasks=[venue_task, 
           logistics_task, 
           marketing_task],
    
    verbose=True
)

@app.get("/")
def read_root():
    return {"Hello": "Crew AI!"}

@app.post("/start_event_planning")
def start_event_planning(event_topic: str, event_description: str, event_city: str, tentative_date: str, expected_participants: int, budget: int, venue_type: str):
    event_details = {
        'event_topic': event_topic,
        'event_description': event_description,
        'event_city': event_city,
        'tentative_date': tentative_date,
        'expected_participants': expected_participants,
        'budget': budget,
        'venue_type': venue_type
    }
    result = event_management_crew.kickoff(inputs=event_details)
    
    return {"message": "Event planning started!", "result": result}
    
    # import json 
    # from pprint import pprint
    
    # with open('venue_details.json') as f:
    #     data = json.load(f)
    #     return {"message": "Event planning started!", "venue_details": data}
    