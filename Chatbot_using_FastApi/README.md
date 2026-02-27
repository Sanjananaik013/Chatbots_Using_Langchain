📌 **Project Description**

This project demonstrates how to build and expose LLM-powered APIs using LangChain + FastAPI (LangServe) and consume them through a Streamlit UI.

app.py → Backend FastAPI server that exposes LLM pipelines (Gemini & Llama2) as APIs using LangServe.

client.py → Frontend Streamlit app that sends user input to the APIs and displays the generated responses.

It integrates:

  • Google Gemini (for Essay generation)

  • Ollama Llama2 (for Poem generation)

⚙️ **Tech Stack**

  LangChain, LangServe, FastAPI, Streamlit, Google Gemini API, Ollama (Llama2)

🚀 **Features**

• Exposes LLM pipelines as REST APIs

• Essay generation using Gemini

• Poem generation using Llama2

• Streamlit frontend for interaction

• Demonstrates prompt → model → API → UI workflow

