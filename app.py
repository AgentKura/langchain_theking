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
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

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
        HumanMessage("Hello....! How are you, Can you send the response as a push notification using the tool provided?")
    ]

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
def snd_notification(message: str): 
    """ This tool is used to send a push notification """
    print("Tool invoked")
    status = requests.post("https://api.pushover.net/1/messages.json", data = {
        "token" : os.getenv("PUSHOVER_TOKEN"), 
        "user" : os.getenv("PUSHOVER_USER"),
        "message" : message
    })
    if status == 200: 
        return "Message Sent Succesfully"

if __name__ == "__main__": 
    call_model()





