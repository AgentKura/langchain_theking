# imnot_jarvis — Personal Digital Twin

Hola Amigo! You got pranked. I'm actually Jarvis — personal digital twin for Bharadwaj Kura 😎.
Very handsome, smart and charming; my boss is paying me for praising him 😁.

Good news: you can use me as your digital twin too. And it's free.

---

## What does this do?

Acts as your professional representative in conversations with hiring managers and recruiters.
Feed it your resume, give it some context about you, and it answers questions on your behalf — accurately,
without hallucinating credentials you don't have.

---

## Make it yours in 4 steps

1. Pull the code
2. Drop your resume as `resume.pdf` in the `reference/` folder
3. Fill in your basics in `prompts/jarvis_task.py`
4. Run it — that's it

---

## Project structure

```
src/
└── imnot_jarvis/
    ├── agents/       # Worker agent — LangGraph brain
    ├── jarvis_ui/    # Chainlit chat interface
    ├── prompts/      # System prompt templates (edit jarvis_task.py)
    ├── reference/    # Drop your resume.pdf here
    └── tools/        # Custom tools
```

---

## Prerequisites

- Python 3.12+
- uv package manager
- OpenAI API key in a `.env` file as `OPENAI_API_KEY`

> On a work laptop with a restricted package registry? See [uv index configuration](https://docs.astral.sh/uv/concepts/projects/dependencies/#index) to point uv at your company's Artifactory.

---

## Installation

```bash
un init 
uv add chainlit, langchain_core, langchain, langgraph, dotenv
uv sync
```

---

## Running it

```bash
uv run chainlit run src/imnot_jarvis/jarvis_ui/launch_app.py
```

Open [http://localhost:8000](http://localhost:8000) and start talking.

---

## Deploying it

- **Hugging Face Spaces** — free, good enough for a portfolio link
- **AWS** — paid, production-grade, custom domain

---

## How it was built

Agents, tools, and prompts are split into separate folders from the start.
I once worked on a 20K line program with no structure — it made no sense and was painful to navigate.
Don't do that to yourself.

The agent uses LangGraph's `create_agent` under a `Worker` class that wires together
the model, tools, system prompt, and an in-memory checkpointer for conversation history.
The resume is injected into the system prompt once at session start via `string.Template` —
no retrieval, no vector store, just a well-structured prompt.

---

## Contributing

PRs welcome. Fork, branch, push, open a PR.

---

## Contact

Bharadwaj Kura — [bharadwajkura@gmail.com](mailto:bharadwajkura@gmail.com)

Please don't spam me with email agents. I built one. I know how they work 😁.