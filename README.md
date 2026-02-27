**Chatbots Using Open Source Api-Keys**

1. The app.py is a file consists of a simple LLM-powered chatbot application built using LangChain, Google Gemini, and Streamlit.

    The application takes a user’s question through a Streamlit interface and sends it to the Gemini model using LangChain’s prompt pipeline. A structured prompt         template is used to guide the model’s response, ensuring helpful and relevant answers.

    The workflow includes:

    • Loading the Gemini API key securely using environment variables

    • Defining a system + user prompt using LangChain's ChatPromptTemplate

    • Connecting to the Gemini model (gemini-2.5-flash) via GoogleGenerativeAI

    • Processing the model output using StrOutputParser

    • Displaying the response interactively through a Streamlit UI
   
    Output -
   <img width="921" height="744" alt="image" src="https://github.com/user-attachments/assets/2e459782-3299-4e0d-90f9-fd38efdf391e" />


3. The Ollama.py file contains a simple chatbot application built using LangChain, Ollama, and Streamlit.
   
    The apllication allows users to ask questions through a web interface and receive responses from the locally running Llama2 language model. 
    It demonstrates how to create an end-to-end LLM pipeline using a prompt template, local model inference, and output parsing — all without relying on external APIs.

   Output-
   <img width="1058" height="399" alt="image" src="https://github.com/user-attachments/assets/5f2aa855-6831-4c0e-8dc5-31129bd2e205" />

