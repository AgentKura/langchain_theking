#  Langchain_TheKing - Multiple Projects using Langchain - Orchestration
## I've tried many SDK's for Agentic AI development. I feel langchain remains the king of all the sdk's I've tried. 

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
### src/langchain_app
    - This folder has code related to Langchain->create_agent method which creats an agent graph out of the box. 
    - More details on create_agent can be found at: https://reference.langchain.com/python/langchain/agents/factory/create_agent
    - Model can be from any provider supported on langchain. Models related to providers can be found at: https://docs.langchain.com/oss/python/integrations/chat?_gl=1*18jv9gm*_gcl_au*NjA4MzA3OTI4LjE3ODQ3MjY2ODE.*_ga*MTM5MTc3MTIyMy4xNzg0NzI2Njgx*_ga_47WX3HKKY2*czE3ODUxODUzNDckbzQkZzEkdDE3ODUxODUzNjgkajM5JGwwJGgw

### src/imnot_jarvis
    - This folder contains code for DigitalTwin App, which can act as your assistant to provide details about your profile. 
    - The agent is build to strictly avoid hallucination.
    - You can independently work on this application. For more details, look into the readme.md file inside the app. 

### src/langgraph_app
    - Graph Orchestration from basics. 
    - This app does not have a UI, you're free to add Gradio/ChainLit/StreamLit as your UI. 
    - This app covers back application which utilizes tools and provide structured outputs. 

## Repository Structure
```
src/
├── imnot_jarvis/           # Digital twin agent
│   ├── agents/             # Worker — wraps create_agent, tools, checkpointer
│   ├── jarvis_ui/          # Chainlit entry point
│   ├── prompts/            # System prompt templates
│   ├── reference/          # Resume / background source material
│   ├── tools/              # Custom tools
│   └── README.md
├── langchain_app/          # LangChain learning module
│   ├── agents/
│   ├── app_ui/
│   ├── prompts/
│   ├── tools/
│   ├── __init__.py
│   └── README.md
├── langchain_core_app/
│   └── app.py
└── langgraph_app/
    ├── app_graph.ipynb
    ├── orch_lang_graph.py
    └── tool.py
```

