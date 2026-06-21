
# AI Meal Planning & Nutrition Agent

An intelligent LLM Agent built with LangChain that dynamically routes tasks between unstructured context retrieval (**RAG**) and deterministic logic (**Structured Math Tools**).

## Key Features
- **Semantic RAG Routing:** Searches a custom vector corpus for high-protein Indian dietary configurations without depending on literal string lookups.
- **Deterministic Tool Calling:** Offloads body mass index (BMI) and gender-specific (Mifflin-St Jeor) basic metabolic math directly to Python utilities, bypassing standard LLM hallucination limits.
- **Fine-grained Macro Ingestion:** Accurately evaluates weights and nutrition structures for high-density ingredients (e.g., Soya Chunks, Paneer, Chicken).

## Installation & Setup
1. Clone the repository and navigate inside:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/ai-nutrition-agent.git](https://github.com/YOUR_USERNAME/ai-nutrition-agent.git)
   cd ai-nutrition-agent
