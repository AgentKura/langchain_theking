#Orchestration with LangGraph. 
#Important things to be considered while using LangGraph. 
"""
1. Graph: Which is similar to a workflow. 
2. State: 
3. Node: Which does the actual work. Action sits in the node. 
4. Edge: Defines order of execution to nodes. 

"""

#import the dependecies first. 
from re import S
from typing import Annotated, TypedDict
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph
from langgraph.graph import add_messages
from langgraph.graph._node import StateNode
from langgraph.graph import END, START
from IPython.display import Image,display
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import ToolNode, tools_condition
from tool import send_notification
from PIL import Image as PILImage
import io
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_community.tools import GoogleSerperRun

#Define a stateclass
class State(TypedDict): 
    messages : Annotated[list,add_messages]

class run_graph(): 

    def __init__(self,tools_prm):
        self.llm = ChatOpenAI(model="gpt-4.1-mini") 
        self.tool_llm = self.llm.bind_tools(tools_prm)


    #Define a Node - remember it's a function, takes the current state and returns the new state
    def dummy_node(self,lv_state: State)->dict: 
        input = lv_state['messages'][0].content
        model_message = [
            HumanMessage(input)
        ]
        llm_response = self.tool_llm.invoke(input = model_message)
        return {'messages': [{"role": "assistant", "content": llm_response.content}]}


if __name__ == "__main__": 
    load_dotenv(override=True) #loads the environment variables. 
    
    search = GoogleSerperRun(api_wrapper=GoogleSerperAPIWrapper())
    llm_tools = [search, send_notification]

    #Define the Graph. 
    lo_run = run_graph(tools_prm=llm_tools)
    lo_graph = StateGraph(State)

    #Add Nodes
    lo_graph.add_node("A",lo_run.dummy_node)
    lo_graph.add_node("tools", ToolNode(llm_tools))

    #Define Edges
    lo_graph.add_edge(START, "A")
    lo_graph.add_conditional_edges("A", tools_condition)
    lo_graph.add_edge("tools","A")

    compiled_graph = lo_graph.compile()

    #png_bytes = compiled_graph.get_graph().draw_mermaid_png()
    #img = PILImage.open(io.BytesIO(png_bytes))
    #img.show()

    result = compiled_graph.invoke({"messages": [{"role": "user", "content": "Can you list the tool schema attatched to you?"}]})
    print(result)
    print(result["messages"][1].content)

