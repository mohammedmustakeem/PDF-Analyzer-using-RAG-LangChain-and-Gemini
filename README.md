# PDF Analyzer — RAG + LangChain + Gemini

PDF Analyzer is an AI-powered application that enables users to upload PDF documents and ask natural language questions about their content. The application uses Retrieval-Augmented Generation (RAG) to generate accurate, context-aware responses grounded entirely in the uploaded document.
The system combines LangChain, Google Gemini, HuggingFace Embeddings, Chroma Vector Database, and Streamlit to create an interactive PDF question-answering experience.Create a seprate environment to get no library version conflict.

---

## Demo

> Upload a resume → Ask "What skills does the candidate have?" → Get a precise, context-grounded answer instantly.

---

## Architecture

```
User uploads PDF
      │
      ▼
 Streamlit UI
      │
      ▼
 PyPDFLoader  ──────────────────────────── Extract raw text
      │
      ▼
 RecursiveCharacterTextSplitter ────────── Split into chunks (1000 chars, 200 overlap)
      │
      ▼
 HuggingFace Embeddings ─────────────────  all-MiniLM-L6-v2
      │
      ▼
 Chroma Vector Store ────────────────────  Persist embeddings locally
      │
      │   ◄── User question
      ▼
 Retriever ──────────────────────────────  Top-K semantic similarity search
      │
      ▼
 Context Builder ────────────────────────  Merge relevant chunks
      │
      ▼
 Prompt Template ────────────────────────  Anti-hallucination system prompt
      │
      ▼
 Google Gemini LLM ──────────────────────  Generate grounded answer
      │
      ▼
 Answer displayed in Streamlit UI
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Document Loader | LangChain PyPDFLoader |
| Text Splitting | RecursiveCharacterTextSplitter |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` |
| Vector Database | Chroma |
| LLM | Google Gemini 1.5 Flash |
| Orchestration | LangChain RetrievalQA |
| Environment | python-dotenv |

---

## Project Structure

```
pdf-analyzer-using-rag-and-langchain/
│
├── main.py              # Streamlit app — full RAG pipeline
├── requirements.txt     # Python dependencies
├── .env.example         # Template for environment variables
├── .gitignore           # Git exclusions
├── chroma_db/           # Auto-generated vector store (git-ignored)
└── README.md
```

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-analyzer-using-rag-and-langchain.git
cd pdf-analyzer-using-rag-and-langchain
```

### 2. Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Open `.env` and add your Google API key:

```
GOOGLE_API_KEY=your_actual_api_key_here
```

Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 5. Run the application

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`.

---

## How to Use

1. **Upload** a PDF using the sidebar file uploader.
2. **Wait** for the ingestion pipeline to process and embed the document.
3. **Ask** any natural language question in the input box.
4. **View** the AI-generated answer along with the source chunks retrieved.

**Example questions for a resume PDF:**
- What skills are mentioned in this resume?
- What projects has the candidate worked on?
- What is the candidate's CGPA?
- Summarize the work experience.
- Which technologies does the candidate know?

---

## Prompt Engineering

The system prompt is designed to minimize hallucinations:

```
You are an expert PDF assistant.
Answer ONLY from the context provided.
Do NOT make assumptions or add external knowledge.
If the answer is not in the context, say:
"I could not find this information in the uploaded PDF."
```

---

## Challenges & Learnings

Building this project involved solving real-world RAG problems:

- Handling PDF temp file paths correctly across OS environments
- Resolving LangChain import conflicts across package versions
- Tuning chunk size and overlap for accurate retrieval
- Preventing Gemini from hallucinating beyond the retrieved context
- Managing Chroma persistence between Streamlit sessions

---

## Future Improvements

- [ ] Multi-PDF support
- [ ] Chat history with memory
- [ ] Source citations with page numbers highlighted
- [ ] Hybrid search (BM25 + Vector)
- [ ] PDF summarization mode
- [ ] Deploy on Streamlit Cloud
- [ ] Docker support
- [ ] Authentication system

---

## Skills Demonstrated

`Retrieval-Augmented Generation` `LangChain` `Streamlit` `Prompt Engineering` `HuggingFace` `Chroma` `Semantic Search` `Google Gemini` `Python` `Vector Databases`

---

## Author

**Mohammed Mustakeem**  
B.Tech — Artificial Intelligence & Machine Learning  
University of Engineering and Management, Jaipur
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](www.linkedin.com/in/mohammed-mustakeem-01229228b)

---

## License

This project is for educational and portfolio purposes.

