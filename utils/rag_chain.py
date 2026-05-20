import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings
from langchain.chains import RetrievalQA
from utils.llm_config import get_llm
import os
def create_rag_chain(chunks):
    #8 embeddings created / converts text into numbers(vectors)
    embeddings = FakeEmbeddings(size=384)
    #9 each embedding stored into vector database that is FAISS(in memory)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    # it save the data into vectorstore
    os.makedirs("Vectorstore", exist_ok=True)
    vectorstore.save_local("Vectorstore")

    #creates a retriever interface (it know how to take query,find similar vectors,return relevant chunks)
    # finds top  relevant chunks
    retriever = vectorstore.as_retriever(search_kwargs={"k": 1}) #arguments
    llm = get_llm()
#creates a RAG Chain
#It creates the full RAG pipeline automatically
#Before using LLM, always retrieve relevant data first
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain
































