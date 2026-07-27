from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph 
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

#classes use pascal case
class Base_Agent:

    def __init__(self): 
        #Python uses Hungarian Notation; so prefixes for variables
        #snake case for variables and objects
        #Leading underscore '_' for variables which are used in local scope and not used anywhere else. 
        #Use TypeHints for strict type clarity. 
        self._llm : CompiledStateGraph #create_agent method returns a Compiled State Graph.
        self._sysprompt: str | SystemMessage | None = None 
        self._aimessage : AIMessage

    def initialize_llm(self, usr_model): 
        self._llm = create_agent(
            model= usr_model,
            system_prompt = self._sysprompt
        )
    
    def set_sys_prompt(self,sys_promt): 
        self._sysprompt = SystemMessage(
            content=sys_prompt
        )

    def get_response(self,usr_prompt): 
        _llm_response = self._llm.invoke(input=usr_prompt)
        self._aimessage = _llm_response['messages'][0]
        print(self._aimessage.content)


if __name__ == "__main__": 
    #Execute actions here
    #Before initializing the Agent, make sure key is passed by overriding the environment variables. 
    load_dotenv(override=True)
    ba_object = Base_Agent()
    sys_prompt = """ You are a System architect for Agentic AI solutions. Your name is 'Richard'. 
    - You are experienced in building Agentic AI workflows.
    - Full Stack applications with Agentic AI Skills and tools. 
    - You're experienced to automate the user tasks on web based applications. 
    - You're experienced in building agents capable of managing infrastructure for small set of virtual machies and services. 

    ## Tasks: 
    - You're currently, acting as a Advisor for Business teams to identify, Analyze and Optimize business process using Agentic AI solutions. 
    - You engage with business owners to understand their redundant processes and provide solutions with Agent AI workflows, skills, tools and MCP's. 
    
    ## Duties: 
    - You ask questions when you need more context from Business owners. 
    - You do not jump into conclusions without full context. 
    - You provide better solutions that require less support in the future. 
    """
    ba_object.set_sys_prompt(sys_promt=sys_prompt)
    ba_object.initialize_llm(usr_model='gpt-4.1-mini')
    usr_message = HumanMessage(content="Hi! How are you doing sir?")
    ba_object.get_response(usr_prompt=usr_message)