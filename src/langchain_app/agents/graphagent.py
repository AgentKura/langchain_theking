# PEP-8 grouping standards - Stdlib, Third party, First party - Seperated by blank-lines
import io
from collections.abc import Sequence, Callable #Standard imports
from typing import Any
from dotenv import load_dotenv
from PIL import Image as PILImage


from langchain.agents import create_agent #Third Party
from langgraph.graph.state import CompiledStateGraph 
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage
from langchain_core.tools import BaseTool,tool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import InMemorySaver

from langchain_app.tools.cflogin_tool import btp_login #First Party

#classes use pascal case
class BaseAgent:

    #Constructor cannot return a co-routine. It has to be synchronous always. 
    def __init__(self): 
        #snake case for variables and objects
        #Leading underscore '_' for variables which are used in local scope and not used anywhere else. 
        #Use TypeHints for strict type clarity. 
        load_dotenv(override=True)
        self._llm : CompiledStateGraph | None = None #create_agent method returns a Compiled State Graph.
        self._sysprompt: str | SystemMessage | None = None 
        self._aimessage : AIMessage | None = None
        self._llm_tools : Sequence[BaseTool | Callable[..., Any] | dict[str, Any]] | None = None
    
    def set_sys_prompt(self, system_prompt:str)->None: 
        self._sysprompt = SystemMessage(
            content = system_prompt
        )

    def define_tools(self,tool:tool): 
        self._llm_tools = [tool]

    #No reason for these methods to be async: 
    #async is for -- Network Calls, disk reads and setting an attribute. 
    def initialize_llm(self, usr_model)->CompiledStateGraph: 
        self._llm = create_agent(
            model= usr_model,
            system_prompt = self._sysprompt,
            tools = self._llm_tools,
            checkpointer=InMemorySaver()
        )
        return self._llm
    
    def get_response(self,usr_prompt)->None: 
        #Define thread id before invoking. 
        thread_config = {"configurable": {"thread_id": "1"}}
        _llm_response = self._llm.invoke(input=usr_prompt,config=thread_config)
        self._aimessage = _llm_response['messages'][-1]
        print(self._aimessage.content)

    def display_graph(self): 
       if self._llm is not None: 
            png_bytes = self._llm.get_graph().draw_mermaid_png()
            img = PILImage.open(io.BytesIO(png_bytes))
            img.show()
