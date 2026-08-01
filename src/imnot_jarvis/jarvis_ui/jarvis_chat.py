# There are many AI Chat libraries out there. However, for me chailit UI seems to be smoother.  
import asyncio
from PyPDF2 import PdfReader

import chainlit as cl
from langgraph.graph.state import CompiledStateGraph
from langgraph.types import GraphOutput
from langchain.messages import HumanMessage
from langgraph.pregel.main import RunnableConfig

from imnot_jarvis.agents.worker import Worker
from imnot_jarvis.prompts.jarvis_task import jarvis_system_prompt



@cl.on_chat_start
async def start_chat():
    #Initialize the worker agent class
    #For now do not set any system prompt, send the model. 
    resume_details: str = ""

    wo_agent = Worker()
    llm_system_prompt = jarvis_system_prompt

    #Extract Resume details from PDF. 
    pdf_extract = PdfReader(stream="4_langchain/src/imnot_jarvis/reference/resume.pdf")
    for page in pdf_extract.pages:
        resume_details += page.extract_text()

    wo_agent.set_system_prompt(
        system_prompt=llm_system_prompt.substitute(candidate_details = resume_details)
    )
    session_agent: CompiledStateGraph | None = wo_agent.initialize_agent(usr_model="gpt-5-mini")

    cl.user_session.set("agent", session_agent)


@cl.on_message
async def on_usr_message(usr_message:cl.Message): 
    #this is what user inputed on the Screen. 
    msg = cl.Message(content="")
    #Get agent reference here and pass the message
    
    wo_agent : CompiledStateGraph | None = cl.user_session.get("agent")

    #maintain a callback to the Agent in the config
    config = RunnableConfig(
        configurable={"thread_id": cl.context.session.id},
        callbacks= [cl.LangchainCallbackHandler()]
    )

    #Output will be of dicts
    async for chunk in wo_agent.astream(
        input = {"messages": [HumanMessage(content=usr_message.content)]},
        config = config,
        stream_mode = "messages"
    ):
        await msg.stream_token(token = chunk[0].content)
    await msg.send()






