# AI Nutrition & Meal Planning Agent

An agent that decides, per question, whether to semantically search a recipe
knowledge base (RAG), look up precise ingredient macros, or calculate
calorie/BMR targets — built with LangChain tool-calling.

## Architecture

| File                | Purpose                                                         |
|---------------------|-------------------------------------------------------------------|
| `data/recipes.txt`  | Recipe knowledge base, one full recipe per line (RAG corpus).    |
| `src/database.py`   | Embeds recipes into a Chroma vector store, exposes a retriever. |
| `src/tools.py`      | Three tools: recipe search (RAG), nutrition lookup, body metrics.|
| `src/agent.py`      | Builds the tool-calling agent (LangChain `AgentExecutor`).       |
| `main.py`           | CLI entry point.                                                 |

**Why this counts as agentic, not just an LLM call:** the agent decides which
of the three tools to use (or none) per question, based on the tool
descriptions — that routing logic isn't hardcoded.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # then edit .env and paste your real key
```

## Run

```bash
python main.py
```

Try asking:
- "Suggest a high-protein vegetarian dinner" → recipe search (RAG)
- "How many calories in 150g paneer?" → nutrition lookup
- "I'm 70kg, 170cm, 28, male, trying to lose weight — what's my target calories?" → body metrics

## Notes / honest limitations

- `lookup_ingredient_nutrition` only has 3 ingredients hardcoded for the demo —
  swap in a real nutrition dataset (e.g. USDA FoodData Central CSV) to extend.
- `calculate_body_metrics` is a basic Mifflin-St Jeor estimate, not medical advice.
- Uses the older LangChain `AgentExecutor` pattern; LangGraph's `create_react_agent`
  is the newer recommended approach if extending this further.

## Resume bullets (once you've run it and tried a few questions)

> **AI Nutrition & Meal Planning Agent**
> - Built a tool-calling agent (LangChain) that routes between RAG-based recipe
>   retrieval and structured nutrition/BMR calculation tools based on query intent
> - Implemented a RAG pipeline over a custom recipe corpus using OpenAI embeddings
>   and a Chroma vector store
> - Designed clear tool-use boundaries: semantic search for unstructured recipe
>   text vs. deterministic lookups for nutrition math
