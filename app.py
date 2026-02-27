from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()
os.environ["GOOGLE_API_KEY"]=os.getenv("LANGCHAIN_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ('system','You are a helpful assistant that responses to user questions'),
        ('user','Question:{Question}')
        
    ]
)

st.title("langchain Chatbt")
input_text=st.text_input("Enter a question")

llm=GoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.9)
outputparser=StrOutputParser()

chain=prompt | llm | outputparser

if input_text:
    st.write(chain.invoke({'Question':input_text}))