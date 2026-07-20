# So far with different AI SDKs - Langchain interested me more. Reasons: 
""" 
- Langchain is in the race since Oct, 2022. 
- Langchain-core gives full control over the Agentic Architecture. 
- Langchain has wider community support. 
- They keep on adding new features: LangGraph, Langchain, Deep Agents.
- They have observability tools: LangSmith. 
"""

#Step 1: import packages. 
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

def call_model(): 
    #Initialize the model. 
    load_dotenv(override=True)
    print(f"Open AI Key is {os.getenv("OPENAI_API_KEY")}")
    openai_model = ChatOpenAI(
        model="gpt-4.1-mini",
        api_key=os.getenv("OPENAI_API_KEY")
    )

    #Now the model needs a message. 
    #langchain is more disciplined - accepts SystemMessage, HumanMessage and AIMessage
    model_messages = [
        HumanMessage("Hello....! How are you?")
    ]

    model_response = openai_model.invoke(model_messages)
    print(model_response.content)

if __name__ == "__main__": 
    call_model()





