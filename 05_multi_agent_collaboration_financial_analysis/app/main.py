from fastapi import FastAPI
from crewai import Crew, Process
from langchain_openai import ChatOpenAI

from app.agents import data_analyst_agent, trading_strategy_agent, execution_agent, risk_management_agent
from app.tasks import data_analysis_task, strategy_development_task, execution_planning_task, risk_assessment_task

app = FastAPI(
    title="Multi Agent Collaboration for Financial Analysis",
    version="0.0.1",
    )

# Define the crew with agents and tasks
financial_trading_crew = Crew(
    agents=[data_analyst_agent, 
            trading_strategy_agent, 
            execution_agent, 
            risk_management_agent],
    
    tasks=[data_analysis_task, 
           strategy_development_task, 
           execution_planning_task, 
           risk_assessment_task],
    
    manager_llm=ChatOpenAI(model="gpt-3.5-turbo", 
                           temperature=0.7),
    process=Process.hierarchical,
    verbose=True
)

@app.get("/")
def read_root():
    return {"Hello": "Crew AI"}


@app.post("/analyze_financial_data")
def analyze_financial_data(stock_selection: str, initial_capital: float, risk_tolerance: str, trading_strategy_preference: str, news_impact_consideration: bool):
    financial_trading_inputs = {
    'stock_selection': stock_selection,
    'initial_capital':  initial_capital,
    'risk_tolerance':  risk_tolerance,
    'trading_strategy_preference':  trading_strategy_preference,
    'news_impact_consideration': news_impact_consideration
    }
    result = financial_trading_crew.kickoff(inputs=financial_trading_inputs)
    
    return {
        "result": result
    }