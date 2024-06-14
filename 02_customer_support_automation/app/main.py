from fastapi import FastAPI

app = FastAPI(
    title="Customer Support Automation CrewAI",
    version="0.0.1",
    )

@app.get("/")
def read_root():
    return {"Hello": "Crew AI"}

