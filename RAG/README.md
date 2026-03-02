📄 Project Description(simplerag.ipynb)

This project implements a simple Retrieval-Augmented Generation (RAG) pipeline using LangChain and Google Gemini embeddings.

🔹 Methods / Components Used

    TextLoader → Used to load content from text file

    PyPDFLoader → Used to load content from pdf file
    
    WebBaseLoader → Used to load content from web URLs

    BeautifulSoup (SoupStrainer) → Used to extract only relevant HTML content

    RecursiveCharacterTextSplitter → Used to split large documents into smaller chunks

    GoogleGenerativeAIEmbeddings (gemini-embedding-001) → Used to convert text into vector embeddings

    Chroma Vector Store → Used to store embeddings for retrieval

    FAISS (optional) → Used for efficient similarity-based search

🔹 Key Steps

    Loads data from sources like web pages, text file and PDF

    Extracts only relevant content using BeautifulSoup

    Splits large text into smaller chunks for processing

    Converts text into vector embeddings using Gemini

    Stores embeddings in vector databases like Chroma / FAISS

    Enables semantic search for retrieving relevant information

📄 Project Description(retriver.ipynb)

This project implements a advanced RAG workflow by seamlessly integrating semantic retrieval and context-aware generation into a structured pipeline on top of simple RAG(which is implemented in simplerag.ipynb).

🔹 Components Used

    create_stuff_documents_chain() → Used to create a document chain that combines retrieved documents with the prompt before sending to the LLM

    as_retriever() → Used to convert the vector store into a retriever for semantic document search

    create_retrieval_chain() → Used to create the retrieval pipeline by combining the retriever and document chain
