import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import time
groq_api_key = os.getenv("GROQ_API_KEY")
from langchain_groq import ChatGroq

from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains import create_retrieval_chain 
from langchain_community.vectorstores import FAISS

if "vector" not in st.session_state:
    st.session_state.embeddings=OllamaEmbeddings()
    st.session_state.loader=WebBaseLoader("https://docs.smith.langchain.com/")
    st.session_state.docs=st.session_state.loader.load()

    st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs)

    st.session_state.vector=FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)

st.title("ChatGroq")

llm=ChatGroq(groq_api_key=groq_api_key,model_name="Gemma-7B-IT")

prompt=ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}

"""
)

document_chain=create_stuff_documents_chain(llm=llm,prompt=prompt)
retriever=st.session_state.vector.as_retriever()

retriever_chain=create_retrieval_chain(retriever,document_chain)


query=st.text_input("Ask a question!!")

if query:
    start=time.process_time()
    response=retriever_chain.invoke({"input":query})
    print("Response Time:",time.process_time()-start)
    st.write(response['answer'])

