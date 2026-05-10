import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import FakeEmbeddings
from langchain.chains import RetrievalQA
from utils.llm_config import get_llm
import os
def create_rag_chain(chunks):
    #8th embeddings created 

    embeddings = FakeEmbeddings(size=384)

    # 9th each embedding stored into vector database that is FAISS(in memory)

    vectorstore = FAISS.from_documents(chunks, embeddings)
    
    # it save the data into vectorstore
     
    os.makedirs("Vectorstore", exist_ok=True)
    vectorstore.save_local("Vectorstore")


    retriever = vectorstore.as_retriever(search_kwargs={"k": 1})

    llm = get_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
































'''import streamlit as st

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from utils.llm_config import get_llm


# ✅ Load embeddings ONLY ONCE (Streamlit-safe)
@st.cache_resource(show_spinner="Loading embedding model...")
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={
            "device": "cpu"   # ✅ REQUIRED on Windows
        },
        encode_kwargs={
            "normalize_embeddings": True  # ✅ Stable similarity
        }
    )


def create_rag_chain(chunks):
    embeddings = load_embeddings()

    # ✅ Build FAISS over ALL HR documents
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # ✅ Allow multiple HR policies to be retrieved
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    llm = get_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain'''





















'''import streamlit as st

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from utils.llm_config import get_llm


# ✅ Cache embeddings so they load ONLY ONCE
@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def create_rag_chain(chunks):
    # 1️⃣ Load embeddings (cached)
    embeddings = load_embeddings()

    # 2️⃣ Create FAISS vector store
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # 3️⃣ Retriever with semantic threshold
    retriever = vectorstore.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 2,               # allow multiple HR policies
            "score_threshold": 0.25
        }
    )

    # 4️⃣ Load LLM (Capgemini Gen Engine)
    llm = get_llm()

    # 5️⃣ Create RAG chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain'''

























'''from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from utils.llm_config import get_llm

def create_rag_chain(chunks):
    # ✅ Offline, stable embeddings for POC
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = FAISS.from_documents(chunks, embeddings)
    #NO threshold when using FakeEmbeddings
    retriever = vectorstore.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={"k": 1, "score_threshold": 0.3}
    )

    llm = get_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain'''

















'''import streamlit as st

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from utils.llm_config import get_llm


# ✅ Cache embeddings so they are loaded only once
@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


def create_rag_chain(chunks):
    # 1️⃣ Load embeddings
    embeddings = load_embeddings()

    # 2️⃣ Create FAISS vector store
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # 3️⃣ Retriever with similarity threshold
    # ✅ Ensures only relevant documents are returned
    retriever = vectorstore.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={
            "k": 1,               # return ONLY the most relevant chunk
            "score_threshold": 0.3  # block weak matches like "hello"
        }
    )

    # 4️⃣ Load LLM (Capgemini Gen Engine / Claude)
    llm = get_llm()

    # 5️⃣ Create RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain'''

















'''from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from utils.llm_config import get_llm
from langchain_openai import OpenAIEmbeddings
def create_rag_chain(chunks):
    embeddings=OpenAIEmbeddings(
        model="amazon.titan-embed-text-v1",
        base_url="https://openai.generative.engine.capgemini.com/v1",
        check_embedding_ctx_length=False,
        api_key="gUwe8hjt6y3ZGXy6zLxs36Xkf6OSv7lj4mL7WTNQ"


    )
    vectorstore = FAISS.from_documents(chunks, embeddings)

    llm = get_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

    return qa_chain'''







'''
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings
from utils.llm_config import get_llm

def create_rag_chain(chunks):
    #embeddings = OpenAIEmbeddings()
    embeddings = OpenAIEmbeddings(
        openai_api_key="gUwe8hjt6y3ZGXy6zLxs36Xkf6OSv7lj4mL7WTNQ",
        openai_api_base="https://openai.generative.engine.capgemini.com/v1"
    )


    vectorstore = FAISS.from_documents(chunks, embeddings)

    llm = get_llm()

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )

    return qa_chain
'''
