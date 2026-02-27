The app.py is a file consists of a simple LLM-powered chatbot application built using LangChain, Google Gemini, and Streamlit.

The application takes a user’s question through a Streamlit interface and sends it to the Gemini model using LangChain’s prompt pipeline. A structured prompt template is used to guide the model’s response, ensuring helpful and relevant answers.

The workflow includes:

  Loading the Gemini API key securely using environment variables

  Defining a system + user prompt using LangChain's ChatPromptTemplate

  Connecting to the Gemini model (gemini-2.5-flash) via GoogleGenerativeAI

  Processing the model output using StrOutputParser

  Displaying the response interactively through a Streamlit UI
