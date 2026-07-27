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
import requests
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from pydantic import BaseModel, Field

class ai_details(BaseModel): 
    service_name : str = Field("Name of the Service")
    cloud_provider: str = Field("Cloud Provider for the Service")
    features: list[str] = Field("Features of the Service")

class ai_details_output(BaseModel): 
    service_details: list[ai_details]


def call_model(): 
    #Initialize the model. 
    load_dotenv(override=True)
    openai_model = ChatOpenAI(
        model="gpt-4.1-mini",
        api_key=os.getenv("OPENAI_API_KEY")
    )

    #Now the model needs a message. 
    #langchain is more disciplined - accepts SystemMessage, HumanMessage and AIMessage
    model_messages = [
        SystemMessage("You are a Agentic AI Engineering expert who provides answers to the user queries on Agentic AI"), 
        HumanMessage("Hello, Can you provide me few AWS Agentic AI developement tools like Bedrock and there usecases in AWS")
    ]

    #Define the Structured output model
    tool_llm = openai_model.with_structured_output(ai_details_output)

    #get the model with the tool and bind to the model. 
    #print(snd_notification.description, snd_notification.name, snd_notification.args)
    tool_llm= openai_model.bind_tools(tools=[snd_notification])

    model_response = tool_llm.invoke(model_messages)
    
    #model_response will contain a array called tool_calls 
    for index, call in enumerate(model_response.tool_calls): 
        if call['name'] == "snd_notification": 
            #Call the function with arguments
            tool_argument = call.get('args', {}).get('message')
            snd_notification.invoke({"message": tool_argument})
            #or snd_notification.invoke(call['args'])

@tool
#Let's define a tool. 
def snd_notification(message: ai_details_output): 
    """ This tool is used to send a push notification """
    for sr_detail in message.service_details: 
        print(f"Service name: {sr_detail.service_name}, CloudProvider: {sr_detail.cloud_provider} & Features: {sr_detail.features} \n")
    status = requests.post("https://api.pushover.net/1/messages.json", data = {
        "token" : os.getenv("PUSHOVER_TOKEN"), 
        "user" : os.getenv("PUSHOVER_USER"),
        "message" : message.service_details
    })
    if status == 200: 
        return "Message Sent Succesfully"

if __name__ == "__main__": 
    call_model()





