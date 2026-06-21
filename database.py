import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

def get_recipe_retriever():
    # Read recipes from text file
    file_path = os.path.join("data", "recipes.txt")
    with open(file_path, "r") as f:
        recipes = f.read().splitlines()

    # Embed and initialize an in-memory vector database
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_store = Chroma.from_texts(recipes, embeddings)
    return vector_store.as_retriever(search_kwargs={"k": 1})