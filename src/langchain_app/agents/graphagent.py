# PEP-8 grouping standards - Stdlib, Third party, First party - Seperated by blank-lines
from collections.abc import Sequence, Callable #Standard imports
from typing import Any
from dotenv import load_dotenv

from langchain.agents import create_agent #Third Party
from langgraph.graph.state import CompiledStateGraph 
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage
from langchain_core.tools import BaseTool,tool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

from langchain_app.tools.cflogin_tool import btp_login #First Party

#classes use pascal case
class Base_Agent:

    def __init__(self): 
        #Python uses Hungarian Notation; so prefixes for variables
        #snake case for variables and objects
        #Leading underscore '_' for variables which are used in local scope and not used anywhere else. 
        #Use TypeHints for strict type clarity. 
        _llm : CompiledStateGraph #create_agent method returns a Compiled State Graph.
        _sysprompt: str | SystemMessage | None = None 
        _aimessage : AIMessage
        _llm_tools : Sequence[BaseTool | Callable[..., Any] | dict[str, Any]] | None = None

    def initialize_llm(self, usr_model): 
        self._llm = create_agent(
            model= usr_model,
            system_prompt = self._sysprompt,
            tools = self._llm_tools,
            checkpointer=InMemorySaver()
        )
    
    def set_sys_prompt(self,sys_promt): 
        self._sysprompt = SystemMessage(
            content=sys_prompt
        )

    def get_response(self,usr_prompt): 

        #Define thread id before invoking. 
        thread_config = {"configurable": {"thread_id": "1"}}
        _llm_response = self._llm.invoke(input=usr_prompt,config=thread_config)
        self._aimessage = _llm_response['messages'][0]
        print(self._aimessage.content)

    def define_tools(self,tool:tool): 
        self._llm_tools = [tool]



if __name__ == "__main__": 
    #Execute actions here
    #Before initializing the Agent, make sure key is passed by overriding the environment variables. 
    load_dotenv(override=True)
    ba_object = Base_Agent()
    sys_prompt = """ You are a System architect for Agentic AI solutions. Your name is 'Richard'. 
    - You are experienced in building Agentic AI workflows.
    - Full Stack applications with Agentic AI Skills and tools. 
    - You're experienced to automate the user tasks on web based applications. 
    - You're experienced in building agents capable of managing infrastructure for small set of virtual machines and services. 

    ## Duties: 
    - You help users to perform actions based on their request. 
    - You act as CLI for the users and authenticate users into their cloud platform. 
    - Create/Update/Manage Services on Cloud Platform. 
    """
    #Set System Prompt and Assign tools
    ba_object.set_sys_prompt(sys_promt=sys_prompt)
    ba_object.define_tools(tool=btp_login)

    #Initialize LLM with tools, System Prompt and Model

    #Call LLM with Memory - Postgres
    ba_object.initialize_llm(usr_model='gpt-5-mini')
    usr_message = HumanMessage(content="Hi! How are you doing sir? Can you log me into BTP Cloud Foundry")
    ba_object.get_response(usr_prompt=usr_message)