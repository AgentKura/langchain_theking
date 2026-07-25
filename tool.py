import requests
import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langgraph.prebuilt import tool_node


@tool
def send_notification(message:str): 
    """ 
    Description: This tool is used to send push notification.  

    Args: 
        message : Sends the message as notification. 
    """
    print(f"tool call successfull: {message}")
    response = requests.post(url="https://api.pushover.net/1/messages.json", data={
        "token": os.getenv("PUSHOVER_TOKEN"),
        "user": os.getenv("PUSHOVER_USER"),
        "message": message
    })
    return response.status_code
