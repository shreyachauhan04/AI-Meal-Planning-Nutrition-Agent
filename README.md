# AI Nutrition & Meal Planning Agent

An agentic AI assistant that decides, per question, whether to semantically search a recipe knowledge base, look up precise ingredient macros, or calculate personalized calorie/BMR targets.

# What is this

Most "AI chatbot" demos just wrap an LLM in a chat window. This project goes a step further: the agent itself decides which tool to use for a given question — it isn't hardcoded if/else logic. Ask it for a recipe idea and it searches a vector database; ask it a nutrition question and it runs a calculation instead. That decision-making is what makes this agentic, not just conversational.

# Features

1. Semantic recipe search (RAG) — recipes are embedded into a vector store and retrieved by meaning, not exact keyword match. "High-protein vegetarian dinner" correctly surfaces relevant recipes even without those exact words appearing.
2. Ingredient nutrition lookup — calculates calories, protein, carbs, and fat for a given ingredient and weight.
3. Body metrics calculator — computes BMI and a personalized calorie target (BMR/TDEE via the Mifflin-St Jeor equation) from basic stats and a goal.
4. Agentic tool routing - the LLM reads each question and picks the right tool (or none) on its own, using LangChain's tool-calling.

# How it works

User question
      │
      ▼
   LLM Agent ── reads the question and decides what's needed
      │
      ├── Recipe/meal idea? ──────► RAG search over recipes.txt (Chroma + OpenAI embeddings)
      ├── Nutrition numbers? ─────► Ingredient lookup tool (structured calculation)
      ├── Calorie/BMI targets? ───► Body metrics tool (Mifflin-St Jeor formula)
      └── General question? ──────► Answered directly, no tool needed

      
## Architecture

| File                | Purpose                                                          |
|---------------------|------------------------------------------------------------------|
| `main.py`           | CLI entry point.                                                 |
| `src/agent.py`      | Builds the tool-calling agent (LangChain `AgentExecutor`).       |
| `src/tools.py`      | Three tools: recipe search (RAG), nutrition lookup, body metrics.|
| `src/database.py`   | Embeds recipes into a Chroma vector store, exposes a retriever.  |
| `data/recipes.txt`  | Recipe knowledge base, one full recipe per line (RAG corpus).    |
| `.gitignore`        |Keeps the API key (.env) and cache files out of version control.  |

**Why this counts as agentic, not just an LLM call:** the agent decides which
of the three tools to use (or none) per question, based on the tool
descriptions — that routing logic isn't hardcoded.

## Setup

git clone https://github.com/shreyachauhan04/AI-Meal-Planning-Nutrition-Agent.git
cd AI-Meal-Planning-Nutrition-Agent

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

Create a .env file in the project root with your OpenAI API key:
OPENAI_API_KEY=your-key-here

## Run

python main.py

# Example questions to try

"Suggest a high-protein vegetarian dinner" → triggers recipe search (RAG)
"How many calories are in 150g of paneer?" → triggers nutrition lookup
"I'm 70kg, 170cm, 28, male, trying to lose weight — what's my target calorie intake?" → triggers the body metrics calculator
"What's a quick breakfast idea?" → recipe search again, different query intent

## Notes / honest limitations

- `lookup_ingredient_nutrition` only has 3 ingredients hardcoded for the demo —
  swap in a real nutrition dataset (e.g. USDA FoodData Central CSV) to extend.
- `calculate_body_metrics` is a basic Mifflin-St Jeor estimate, not medical advice.
- Uses the older LangChain `AgentExecutor` pattern; LangGraph's `create_react_agent`
  is the newer recommended approach if extending this further.

#  What I'd build next

Persist the vector store instead of rebuilding it each run
Add a pantry-tracking tool so recipe suggestions prioritize what's already on hand
Swap the hardcoded nutrition lookup for a real food database API

