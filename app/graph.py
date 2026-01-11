import os
import certifi
os.environ['SSL_CERT_FILE']=certifi.where()
from typing import TypedDict, List
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, END

# Setup Env
load_dotenv()
llm=ChatGroq(
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

# Define the state
class AgentState(TypedDict):
    user_craving:str 
    analysis:str 
    final_recipe:str

# Node 1- Identifying the Problem
def analyze_craving(state: AgentState):
    print(f"Analyzing: {state['user_craving']}")

    prompt=ChatPromptTemplate.from_template(
        "You are a Nutritionalist. Check if this input is a valid food item: {craving}. "
        "If it is NOT a food item (like numbers colours, location, restaurant names, or random characters, or colours that aren't flavours), just reply with exactly 'INVALID FOOD ITEM'. "
        "If it is a food, do not say 'It is valid', Just go straight, Identifying 3 unhealthy ingredients/methods usually used in it. "
        "Keep it short. "
    )
    chain=prompt | llm
    response=chain.invoke({"craving": state['user_craving']})

    # Update the state with analysis
    return {"analysis": response.content}

# Node 2- Creating Solution
def generate_recipe(state: AgentState):
    print(f"Cooking up heathly version...")

    prompt= ChatPromptTemplate.from_template(
        "User Craving: {craving}. \n"
        "Nutrional Analysis: {analysis}. \n"
        "Task: Create a healthy, delicious alternative recipe. "
        "Give it a creative name. List the ingredients and short steps."
    )
    chain=prompt | llm
    response=chain.invoke({
        "craving": state['user_craving'],
        "analysis": state['analysis']
    })
    return {"final_recipe": response.content}
def decide_next_step(state: AgentState):
    # Check what analyst wrote
    analysis= state["analysis"]

    # if analyst said its invalid
    if "INVALID" in analysis:
        return "end"
    else:
        return "continue"

# Build the graph
workflow= StateGraph(AgentState)

# Add Nodes
workflow.add_node("analyst", analyze_craving)
workflow.add_node("chef", generate_recipe)

# Add Edges
workflow.set_entry_point("analyst") # start here
workflow.add_conditional_edges(
    "analyst", # start analyst
    decide_next_step, # Run the logic
    {
        "continue": "chef", # if a valid input, then continue to go to chef
        "end": END # If invalid input, then end
    }
)
workflow.add_edge("chef", END) # fin

# compile graph
app=workflow.compile()