from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
load_dotenv()
from langserve import add_routes
import uvicorn
from fastapi import FastAPI

os.environ["GOOGLE_API_KEY"]=os.getenv("LANGCHAIN_KEY")

app=FastAPI(
    title="Langchain API",
    description="API for Langchain LLMs",
    version="1.0"
    
)

add_routes(app,GoogleGenerativeAI(model="gemini-2.5-flash"),path="/google-genai")

model1=GoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.9)
model2=Ollama(model="llama2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(
    app,
    prompt1|model1,
    path="/essay"


)

add_routes(
    app,
    prompt2|model2,
    path="/poem"


)
if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)