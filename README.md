# langchain_theking

A collection of agentic AI projects built with LangChain, LangGraph, and Chainlit.

## Projects

### `src/imnot_jarvis` — Digital Twin Agent
A conversational AI assistant that answers questions about a candidate's professional profile. Reads a PDF resume at startup and uses it as the sole source of truth — no hallucination, no fabrication.

- **Stack:** LangChain · Chainlit · OpenAI · pypdf
- **Architecture:** `Worker` class wraps the agent graph. System prompt is injected once at session start with the extracted resume text. UI streams responses token by token.
- **Detailed docs:** `src/imnot_jarvis/README.md`

### `src/langchain_app` — LangChain Agent with Tools
An agent built using LangChain's `create_agent` factory. Covers tool binding, prompt engineering, and structured outputs.

- **Stack:** LangChain · Chainlit
- **Reference:** [LangChain create_agent docs](https://reference.langchain.com/python/langchain/agents/factory/create_agent)

### `src/langgraph_app` — LangGraph Orchestration
Graph-based orchestration from scratch using LangGraph. Covers state machines, tool nodes, conditional edges, and structured Pydantic outputs. No UI — add Chainlit, Gradio, or Streamlit as needed.

- **Stack:** LangGraph · Pydantic

### `src/langchain_core_app` — LangChain Core
Minimal LangChain Core usage without the higher-level abstractions.

---

## Prerequisites

- Python `>=3.12` — [python.org](https://www.python.org/downloads/)
- uv — [installation guide](https://docs.astral.sh/uv/getting-started/installation/)
- OpenAI API key

---

## Setup

```bash
# 1. Clone the repo
git clone https://github.com/AgentKura/langchain_theking.git
cd langchain_theking

# 2. Install dependencies
uv sync

# 3. Create a .env file in the repo root
echo "OPENAI_API_KEY=your-key-here" > .env
```

---

## Running the projects

**imnot_jarvis (Digital Twin)**
```bash
# Drop your resume PDF at:
# src/imnot_jarvis/reference/resume.pdf

uv run chainlit run src/imnot_jarvis/jarvis_ui/jarvis_chat.py
```
Opens at `http://localhost:8000`

**langgraph_app**
```bash
uv run src/langgraph_app/orch_lang_graph.py
```

**langchain_core_app**
```bash
uv run src/langchain_core_app/app.py
```

---

## Repository structure

```
langchain_theking/
├── src/
│   ├── imnot_jarvis/
│   │   ├── agents/             # Worker class — agent graph, tools, checkpointer
│   │   ├── jarvis_ui/          # Chainlit entry point
│   │   ├── prompts/            # System prompt templates
│   │   ├── reference/          # Resume PDF (not committed — add your own)
│   │   ├── tools/              # Custom tools
│   │   └── README.md
│   ├── langchain_app/
│   │   ├── agents/
│   │   ├── app_ui/
│   │   ├── prompts/
│   │   ├── tools/
│   │   └── README.md
│   ├── langchain_core_app/
│   │   └── app.py
│   └── langgraph_app/
│       ├── app_graph.ipynb
│       ├── orch_lang_graph.py
│       └── tool.py
├── .env                        # Not committed — create from the setup step above
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Tech stack

| Layer | Library |
|---|---|
| Agent orchestration | LangChain, LangGraph |
| LLM provider | OpenAI (GPT) |
| UI | Chainlit |
| PDF parsing | pypdf |
| Package management | uv |

---

## What this is not

Each project here is a self-contained learning artifact — not a production service. No authentication, no persistent storage, no CI. The `imnot_jarvis` agent reads a single PDF and operates entirely in-session memory.