# from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import os
import streamlit as st



prompt=ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful assistant that responses to user questions'),
        ('user','Question:{Question}')
    ]
)

st.title("langchain Chatbot using Ollama")
input_text=st.text_input("Enter a question")

llm=Ollama(model="llama2")
outputparser=StrOutputParser()

chain=prompt | llm | outputparser

if input_text:
    st.write(chain.invoke({'Question':input_text}))
