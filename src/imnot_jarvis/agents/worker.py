# PEP-8 Standards: Standard inputs, Thirdparties & First parties - Seperated by Blank space. 
from dotenv import load_dotenv
from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph
from langchain.messages import SystemMessage

class Worker: 

    #Constructor
    def __init__(self) -> None:
        load_dotenv(override=True)
        self._sys_prompt : str | SystemMessage | None = None 
        self._llm : CompiledStateGraph | None = None
        
    def initialize_agent(self,usr_model)-> CompiledStateGraph: 
        #Let User interface layer select the model. 
        self._llm = create_agent(
            model = usr_model,
            system_prompt= self._sys_prompt
        )
        #Agent is ready. 
        return self._llm

    def set_system_prompt(self,system_prompt): 
        self._sys_prompt = system_prompt


