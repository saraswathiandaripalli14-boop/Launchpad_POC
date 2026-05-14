import streamlit as st
from utils.document_loader import load_documents
from utils.chunking import split_documents
from utils.rag_chain import create_rag_chain

# 1st this line will excute the first and display in UI page like company policy Q&A BOT

st.set_page_config(page_title="Company Policy Q&A Bot")
st.title(" Company Policy Q&A Bot")

#2nd  if execute and load all the documents and it will goto document_loader file and 
# load all the documents there
# this is for Load all documents ONCE 

if "documents" not in st.session_state:

    # 5th •	All policy documents are loaded into memory in documents_loader
    # and store in below line this happens only once, not on every question
   
    st.session_state.documents = load_documents("policydata")

documents = st.session_state.documents

query = st.text_input("Ask a policy question:")

if query:
    q = query.lower()

   
    # DETERMINISTIC POLICY ROUTING (KEY FIX)
    # 6th when user enters a question then it will search the policy type 
    # and select that policy type only remaning policy ignore 
    if "leave" in q:
        filtered_docs = [d for d in documents if "leave" in d.metadata["policy_type"]]

    elif "work from home" in q or "wfh" in q or "office" in q or "remote" in q:
        filtered_docs = [d for d in documents if "work" in d.metadata["policy_type"]]

    elif "expense" in q or "reimbursement" in q:
        filtered_docs = [d for d in documents if "expense" in d.metadata["policy_type"]]

    else:
        filtered_docs = []

    
    # this for handling OUT-OF-CONTEXT data
   
    if not filtered_docs:
        st.warning("I could not find this information in the provided documents.")
    else:
        chunks = split_documents(filtered_docs)
        qa_chain = create_rag_chain(chunks)

        #10th quesry converted into embeddings and search data in FAISS it retrieved only relevent chunks from vector DB
        #11th that chunks give to the LLM that generated a answer to use

        #this line run the chain which the code in rag_chain.py
        #when user ask a question the query is send to rag_chain
        result = qa_chain(query)

        #12th this will display the answer
        
        st.success("Answer:")
        st.write(result.get("result", ""))

        st.markdown("###  Source:")
        
        # 13th this will display the source faile
        sources = result.get("source_documents", [])
        if sources:
            st.write(sources[0].metadata.get("source", "Unknown"))
        else:
            st.write("No source document found")