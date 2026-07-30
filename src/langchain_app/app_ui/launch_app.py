# PEP-8 grouping standards - stdlib, Third party, First party - Seperated By Blank
import chainlit as cl
from typing import cast

from langchain_core.messages import AIMessageChunk, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.base import Runnable

from langchain_app.agents.graphagent import BaseAgent
from langchain_app.prompts.system_prompts import btp_cli_assistant
from langchain_app.tools.cflogin_tool import btp_login
from langgraph.graph.state import RunnableConfig


@cl.on_chat_start
async def on_chat_start(): 
    #This function gets triggered when a chat is initialized. 
    #Initialize the Base Agent. 
    #Define tools
    #AgentGraph takes Disciplined messages and yield StateDicts.
    ba_agent = BaseAgent()
    ba_agent.set_sys_prompt(system_prompt=btp_cli_assistant)
    ba_agent.define_tools(tool=btp_login)
    chat_agent = ba_agent.initialize_llm(usr_model="gpt-5-mini") #Model is Compiled StateGraph
 
    cl.user_session.set("agent",chat_agent)

@cl.on_message
async def on_message(message: cl.Message): 
    chat_agent = cl.user_session.get("agent")
    msg = cl.Message(content="")

    config = RunnableConfig(
        configurable={"thread_id": cl.context.session.id},
        callbacks=[cl.LangchainCallbackHandler()]
    )

    async for chunk in chat_agent.astream(
        input = {"messages": [HumanMessage(message.content)]},
        config = config,
        stream_mode = "messages"
    ): 
        ai_message = chunk[0]
        await msg.stream_token(ai_message.content)
    await msg.send()




