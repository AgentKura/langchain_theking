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
from langgraph.graph import StateGraph
from langgraph.graph import add_messages
from langgraph.graph._node import StateNode
from langgraph.graph import END, START
from IPython.display import Image,display

#Define a stateclass
class State(TypedDict): 
    messages : Annotated[list,add_messages]

#Define a Node - remember it's a function, takes the current state and returns the new state
def dummy_node(lv_state: State)->dict: 
    print(lv_state)
    return {"messages": [{"role": "assistant", "content": "I did say something"}]}


if __name__ == "__main__": 
    lo_graph = StateGraph(State)
    lo_graph.add_node("A",dummy_node)
    lo_graph.add_edge(START, "A")
    lo_graph.add_edge("A",END)
    compiled_graph = lo_graph.compile()

    result = compiled_graph.invoke({"messages": [{"role": "user", "content": "Say Something"}]})
    print(result["messages"][1].content)

