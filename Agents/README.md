📘 Agents.ipynb

    Implemented a multi-tool LLM agent using LangChain.

    Integrated Gemini (gemini-2.0-flash) via ChatGoogleGenerativeAI for reasoning and tool-calling.

    Built a RAG pipeline using:

      WebBaseLoader

      RecursiveCharacterTextSplitter

      GoogleGenerativeAIEmbeddings

      Chroma vector store

    Created custom tools:

      Wikipedia API tool

      Arxiv API tool

      LangSmith documentation retriever tool

    Used create_agent + AgentExecutor for dynamic tool selection and orchestration.

    Enabled semantic search + external knowledge augmentation.

    Implemented secure API key handling via .env.
