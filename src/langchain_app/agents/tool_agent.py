from langchain.agents import create_agent
from langgraph.graph.state import CompiledStateGraph 
from langchain_core.messages import SystemMessage,HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import asyncio


class Tool_Agent(): 
    def __init__(self,llm_model): 
        self._sys_prompt = """
        - You are a helpful SAP BTP Assistant. 
        - You act as a command line for logging into SAP BTP and SAP BTP Cloud Foundry. 
        - You help user to perform following activites. 
            1. Logging into SAP BTP Cloud Foundry. 
            2. Display available services in SAP BTP Cloud Foundry. 
            3. Create/Update/Delete Services, spaces user is authenticated to. 
            4. Perform actions user is authenticated to doing on SAP BTP Cloud Foundry. 
            5. You execute the commands based on standard documentation and avilable in Cloud foundry CLI. 
            6. You be transparent to the user and display the commands you've executed to the user. 
        """
        self._llm = create_agent(
            model = llm_model,
            system_prompt=self._sys_prompt
        )

    def invoke_model(self,usr_input)->AIMessage: 
        _llm_response = asyncio.run(self._llm.ainvoke(
            input = usr_input
        ))
        return _llm_response['messages'][0]