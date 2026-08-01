# There are many AI Chat libraries out there. However, for me chailit UI seems to be smoother.  
import asyncio

import chainlit as cl

from imnot_jarvis.agents.worker import Worker
from langchain.messages import HumanMessage
from langgraph.pregel.main import RunnableConfig

@cl.on_chat_start
async def start_chat():
    #Initialize the worker agent class
    #For now do not set any system prompt, send the model. 
    wo_agent = Worker()
    session_agent = wo_agent.initialize_agent(usr_model="gpt-5-mini")

    cl.user_session.set("agent", session_agent)

@cl.on_message
async def on_usr_message(usr_message:cl.Message): 
    #this is what user inputed on the Screen. 
    msg = cl.Message(content="")
    #how shall I pass this message to the Agent. 
    #Get agent reference here. 
    
    wo_agent = cl.user_session.get("agent")

    #maintain a callback to the Agent in the config
    config = RunnableConfig(
        configurable={"thread_id": cl.context.session.id},
        callbacks= [cl.LangchainCallbackHandler()]
    )

    #Output will be of dicts
    agent_response = await wo_agent.ainvoke(
        input = {"messages": [HumanMessage(content=usr_message.content)]},
        config = config
    )
    final_response = agent_response["messages"][-1]
    await cl.Message(content=final_response.text).send()






