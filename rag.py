from typing import List

import ollama
from langchain_community.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings

ollama_models = ollama.list()
print("OLLAMA RAW LIST:", ollama_models) 
models = []

for m in ollama_models.get("models", []):
    name = m.get("name") or m.get("model") or m.get("model_name")
    if name:
        models.append(name)

print("AVAILABLE MODELS:", models)

BASE_OLLAMA_MODEL = input(f"Choose an OLLAMA model: {models}\n>>> ")

def build_rag(docs: List[str]):
    docs = [Document(page_content=doc) for doc in docs]
    return Chroma.from_documents(documents=docs, embedding=OllamaEmbeddings(model=BASE_OLLAMA_MODEL))

def search_rag(rag, query: str, k=1, **kwargs):
    result = rag.similarity_search_with_score(query, k=k, **kwargs)
    return result[0][0].page_content # NOTE: use a threshold to filter results on the score (i.e. result[0][1] cosine distance)

def create_prompt(context: str, question: str):
    return f"Given the following context: \n\t{context} \n\nAnswer this question: \n\t{question}"

def get_ollama_llm(name: str, **kwargs):
    return Ollama(model=name, **kwargs)

def ask_llm(prompt: str):
    llm = get_ollama_llm(BASE_OLLAMA_MODEL)
    return llm.invoke(prompt)

if __name__ == "__main__":
    # -- example usage
    # local documents for RAG
    docs = [
        "Zeynep Col has lived in NYC for 10 years.",
        "zeynep col is an imaginery LLM engineer in the movive 'The Matrix'.", # intentional typo
        "New York City's subway system is the oldest in the world.",
    ]
    rag = build_rag(docs)

  while True:
        question = input("\n\nEnter a question:\n> ")
        print(f"\n\nUSER QUESTION>>>\n\t{question}")
        context = search_rag(rag, question, k=1)
        print(f"FOUND RAG CONTEXT>>>\n\t{context}")
        prompt = create_prompt(context, question)
        print(f"LLM PROMPT>>> \n\n```\n{prompt}\n```\n\n")
        answer = ask_llm(prompt)
        print(f"LLM RESPONSE:\n\n{answer}")
