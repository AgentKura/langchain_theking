## langchain_theking : I've tried many SDK's for Agentic AI development. So far I feel langchain remains the king of all the sdk's I've tried. 

## Tech Statck Used: 
    - So far, I've developed the initial agent orchestrations through individual python files. 
    - Plan is to include UI, React or any libraries that support chatbot's in the future. 

## Prerequisites: 
    - Install Python, I recommend version >=3.12
    - Install UV - Package manager for Python from Astral Docs: https://docs.astral.sh/uv/getting-started/installation/
    - Below are the usefull UV commands to kickstart the project
```bash
# initialize pyproject.toml file
uv init

# Add Dependancies to the project. 
uv add langchain-core
uv add langgraph
uv add langchain-openiai

# Explicity sync the environment. 
uv sync

# Run a python file. 
uv run file_name.py
```


