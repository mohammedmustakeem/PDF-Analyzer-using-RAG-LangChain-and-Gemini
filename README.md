# PDF-Analyzer-using-RAG-LangChain-and-Gemini
PDF Analyzer is an AI-powered application that enables users to upload PDF documents and ask natural language questions about their content. The application uses Retrieval-Augmented Generation (RAG) to generate accurate, context-aware responses grounded entirely in the uploaded document.
The system combines LangChain, Google Gemini, HuggingFace Embeddings, Chroma Vector Database, and Streamlit to create an interactive PDF question-answering experience.
##Features
Upload and analyze PDF documents.
Ask questions in natural language.
Retrieve relevant information using semantic search.
Generate context-grounded responses.
Display retrieved source chunks.
Persist embeddings locally using Chroma.
Interactive user interface built with Streamlit.
##Technology Stack
| Component              | Technology                     |
| ---------------------- | ------------------------------ |
| Frontend               | Streamlit                      |
| Document Loader        | LangChain PyPDFLoader          |
| Text Splitting         | RecursiveCharacterTextSplitter |
| Embeddings             | HuggingFace all-MiniLM-L6-v2   |
| Vector Database        | Chroma                         |
| Retrieval Framework    | LangChain RetrievalQA          |
| Large Language Model   | Google Gemini 1.5 Flash        |
| Environment Management | python-dotenv                  |
| Programming Language   | Python                         |



