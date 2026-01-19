<h1 align="center">RAG System with Ollama & LangChain</h1>

## 📌 Project Overview
This repository contains a **Retrieval-Augmented Generation (RAG)** implementation built with **LangChain**, **ChromaDB**, and **Ollama**.

The project demonstrates how a local LLM can answer user questions by retrieving relevant context from a small set of documents stored in a vector database.

This implementation focuses on **core RAG concepts** rather than full-scale optimization or sector-specific experimentation.

## ⚙️ Technologies Used
- **LangChain** – RAG pipeline and LLM interface  
- **ChromaDB** – Vector store for similarity search  
- **Ollama** – Local LLM runtime  
- **Ollama Embeddings** – Vector embeddings for documents  

## 🧠 How the RAG System Works
1. A set of local documents is defined in the script  
2. Documents are converted into embeddings using **OllamaEmbeddings**  
3. Embeddings are stored in **ChromaDB**  
4. User questions are matched against the vector store  
5. The most relevant document is retrieved  
6. The retrieved context is injected into the LLM prompt  
7. The LLM generates an answer based on the retrieved context

## 🧪 Example Documents
- Zeynep Col has lived in NYC for 10 years.
- Zeynep Col is an imaginary LLM engineer in the movie 'The Matrix'.
- New York City's subway system is the oldest in the world.

<h1 align="left">Runtime Flow & Output</h2>

## ▶️ Runtime Flow
When the script is executed, the following steps occur in order:

- Available Ollama models are listed from the local Ollama runtime  
- The user selects a model interactively  
- The user enters questions in a continuous loop  
- The system retrieves the most relevant document from ChromaDB  
- The retrieved context is injected into the LLM prompt  
- The LLM generates and prints the final response  

## 📊 Output Section
During execution, the program prints:

- The user question  
- The retrieved RAG context  
- The final prompt sent to the LLM  
- The LLM-generated response  

This output flow makes it easy to observe how retrieval affects the final answer.

## 📊 Output Image

![Image](https://github.com/user-attachments/assets/221fe70f-b5b5-477f-bd94-7d1bed65b59f)

## 🏁 Summary
This runtime-focused README documents the interactive behavior and output structure of the RAG system.  
It complements the main README by explaining how the system behaves during execution and how retrieved context influences LLM responses.

## 🤝 Contributing

Contributions are welcome! 

## 📡 Contact
For any queries or collaborations, feel free to reach out!

🌐 GitHub: [zeynepcol](https://github.com/zeynepcol)  
👤 LinkedIn: [zeynep-col](https://linkedin.com/in/zeynep-col/)
