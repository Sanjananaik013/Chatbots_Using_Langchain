📄 Project Description

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
