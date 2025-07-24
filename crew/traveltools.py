import os
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool

load_dotenv()
tavily_api_key = os.getenv("TAVILY_API_KEY")
search_instance = TavilySearchResults(api_key=tavily_api_key)

@tool
def tavily_search_tool(query: str) -> str:
    """Searches the web using Tavily API and returns top 3 results."""
    results = search_instance.run(query)
    return "\n\n".join([r["content"] for r in results[:3]])
