import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tempfile
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI



st.title("PDF Analyzer")
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI( model="gemini-2.5-flash",google_api_key=GOOGLE_API_KEY ,temperature=0.2)
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_filepath = temp_file.name

    loader = PyPDFLoader(temp_filepath)
    document = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    documnets = text_splitter.split_documents(document)
    embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore=Chroma.from_documents(documents=documnets,embedding=embeddings,persist_directory="./chroma_db")
    retriever = vectorstore.as_retriever(search_type="mmr",search_kwargs={"k": 5})
    question=st.text_input("Ask a question about the PDF:")
    
    if question:
        results=retriever.invoke(question)
        st.write(f"Top 5 relevant chunks:{results}")
        context="\n\n".join( doc.page_content for doc in results)
        prompt = f"""You are an expert PDF assistant. Answer ONLY from the context provided below. If the answer is not present in the context, say: "I could not find this information in the PDF."
        Context:
        {context}
        Question:
        {question} """
        response = llm.invoke(prompt)
        st.write(f"Answer: {response.content}")
  


    st.write(f"Total Pages: {len(document)}")

    st.write(documnets[0].page_content[:1000])
    st.write(documnets[0].metadata)

