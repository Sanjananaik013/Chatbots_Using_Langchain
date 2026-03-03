**Key Points-**

• Developed a Streamlit-based RAG application integrating Groq LLM via ChatGroq (Gemma-7B-IT model).

• Loaded environment variables securely using dotenv and accessed GROQ_API_KEY.

• Implemented web data ingestion using WebBaseLoader (LangSmith documentation source).

• Applied text chunking with RecursiveCharacterTextSplitter (chunk_size=1000, overlap=200).

• Generated embeddings using OllamaEmbeddings.

• Built a FAISS vector store for semantic similarity search.

• Converted vector store into a retriever using .as_retriever().

• Constructed a RAG pipeline using create_stuff_documents_chain and create_retrieval_chain.

• Designed a custom ChatPromptTemplate for context-aware question answering.

• Measured response time using time.process_time() and displayed results via Streamlit UI.
