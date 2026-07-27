##  langchain_theking : I've tried many SDK's for Agentic AI development. I feel langchain remains the king of all the sdk's I've tried. 

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
uv add langchain

# Explicity sync the environment. 
uv sync

# Run a python file. 
uv run file_name.py
```

## Folders
### src/langchain
    - This folder has code related to Langchain->create_agent method which creats an agent graph out of the box. 
    - More details on create_agent can be found at: https://reference.langchain.com/python/langchain/agents/factory/create_agent
    - Model can be from any provider supported on langchain. Models related to providers can be found at: https://docs.langchain.com/oss/python/integrations/chat?_gl=1*18jv9gm*_gcl_au*NjA4MzA3OTI4LjE3ODQ3MjY2ODE.*_ga*MTM5MTc3MTIyMy4xNzg0NzI2Njgx*_ga_47WX3HKKY2*czE3ODUxODUzNDckbzQkZzEkdDE3ODUxODUzNjgkajM5JGwwJGgw

### Class Base_Agent: 
    - Acts as the wrapper around the LLM Calls and performs the actual LLM Calls. 
    - Abstraction layer; which is seperate from core logic can be written in seperate file. For now I've written the abstraction layer in the same file. 
