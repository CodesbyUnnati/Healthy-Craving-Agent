import os
import certifi
os.environ['SSL_CERT_FILE']=certifi.where()
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load the secret keys
load_dotenv()

# Verify Key Exists
api_key= os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("API Key not found! Please add it in you .env file.")

# Using Llama3, as it is free and fast
llm= ChatGroq(
    temperature=0.7,
    groq_api_key=api_key,
    model_name="llama3-8b-8192"
)

# Testing
question= "I am craving Veg Momos. Give me suggestion for a healthy swap option."
print(f"User: {question}")
print("Agent Thinking....")

response=llm.invoke(question)

print(f"Agent: {response.content}")