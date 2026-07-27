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
from typing import Annotated, Callable, Sequence, TypedDict
from langchain_core.messages import HumanMessage, AIMessage
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
from langchain_core.tools import BaseTool
from langchain_core.runnables import Runnable
from langchain_core.language_models import LanguageModelInput
from collections.abc import (
    Sequence,
    Callable
)
from typing import Any

#Define a stateclass
class State(TypedDict): 
    messages : Annotated[list,add_messages]

class run_graph(): 

    def __init__(self):

        # Initialize Variables
        self.lo_graph: StateGraph
        self.llm: ChatOpenAI
        self.tool_llm : Runnable[LanguageModelInput, AIMessage]

    def initialize_graph(self)-> StateGraph: 
        self.lo_graph = StateGraph(State)
        return self.lo_graph

    def initialize_llm(self): 
        self.llm = ChatOpenAI(model = "gpt-4.1-mini")

    def llm_bind_tools(self,llm_tools: Sequence[dict[str, Any] | type | Callable | BaseTool] ): 
        #Accept tools only in pre-defined format in the function. 
        #Bind tools to the llm. 
        self.tool_llm = self.llm.bind_tools(tools=llm_tools)

    #Define a Node - remember it's a function, takes the current state and returns the new state
    def dummy_node(self,lv_state: State)->dict: 
        llm_response = self.tool_llm.invoke(lv_state['messages'])
        return {'messages': [llm_response]}

    def add_nodes(self,node_tools): 
        #Add nodes to the graph
        self.lo_graph.add_node("A", self.dummy_node)
        self.lo_graph.add_node("tools", ToolNode(node_tools))

    def add_edges(self): 
        #Add Edge Conditions
        self.lo_graph.add_edge(START,"A")
        self.lo_graph.add_conditional_edges("A", tools_condition)
        self.lo_graph.add_edge("tools", "A")
    
    def get_compiled_graph(self):
        #Return Compiled Graph 
        return self.lo_graph.compile()

    def draw_graph(self, compiled_graph):
        png_bytes = compiled_graph.get_graph().draw_mermaid_png()
        img = PILImage.open(io.BytesIO(png_bytes))
        img.show()

if __name__ == "__main__": 
    load_dotenv(override=True) #loads the environment variables. 
    
    search = GoogleSerperRun(api_wrapper=GoogleSerperAPIWrapper()) #Tool 1
    node_tools = [search, send_notification] #Tools
    
    lo_run_graph = run_graph()  #Initialize the run_graph class
    lo_run_graph.initialize_graph() #Initialize the Graph   
    lo_run_graph.initialize_llm()   #Initialize LLM Inside the class. 

    #Bind tools to the LLM. 
    lo_run_graph.llm_bind_tools(node_tools)

    #Add Nodes
    lo_run_graph.add_nodes(node_tools=node_tools)
    lo_run_graph.add_edges()

    compiled_graph = lo_run_graph.get_compiled_graph()

    user_qury = """Search for in which state of United States does Boston City exitst using Search tool, 
                  Generate the response in single line. 
                  Send the single line as the response using Send Notification tool"

    """
    result = compiled_graph.invoke({"messages": [{"role": "user", "content":user_qury }]})
    print(result["messages"][-1].content)

