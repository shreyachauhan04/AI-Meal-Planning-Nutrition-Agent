from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from src.tools import search_recipe_database, lookup_ingredient_nutrition, calculate_body_metrics

def create_nutrition_agent():
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    tools = [search_recipe_database, lookup_ingredient_nutrition, calculate_body_metrics]
    
    # Give the agent clear context on its personality and capabilities
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an AI Specialist Nutrition and Meal Planning Assistant. "
                   "Always use the provided tools to fetch recipes, compute math, or lookup macros. "
                   "For general concepts, respond conversationally."),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)