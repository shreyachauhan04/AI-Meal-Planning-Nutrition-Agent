import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Resolve the path relative to the project root, not the current working
# directory -- so this works whether you run `python main.py` from the repo
# root or from inside src/.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RECIPES_PATH = os.path.join(BASE_DIR, "data", "recipes.txt")


def get_recipe_retriever():
    # Read recipes from text file -- one full recipe per line, so each line
    # becomes one chunk and retrieval never returns half a recipe.
    with open(RECIPES_PATH, "r") as f:
        recipes = [line.strip() for line in f if line.strip()]

    # Embed and initialize an in-memory vector database
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = Chroma.from_texts(recipes, embeddings)
    return vector_store.as_retriever(search_kwargs={"k": 2})
