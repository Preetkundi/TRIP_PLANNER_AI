# crew/agents.py
from crewai import Agent
from langchain_ollama import ChatOllama  # pip install langchain-ollama

# LLM
ollama_llm = ChatOllama(model="ollama/llama3", temperature=0.2)

# 🗺️ Itinerary Planner
planner_agent = Agent(
    role="Itinerary Planner",
    goal="Design an optimized and personalized travel itinerary",
    backstory="An expert in planning fun, budget-friendly, and well-balanced travel routes.",
    llm=ollama_llm,
    verbose=True,
)

# 🧑‍🏫 Local Guide
guide_agent = Agent(
    role="Local Cultural Guide",
    goal="Give authentic cultural advice and food/local tips",
    backstory="A native expert who knows hidden gems, local cuisines, and customs to help travelers enjoy deeply.",
    llm=ollama_llm,
    verbose=True,
)
