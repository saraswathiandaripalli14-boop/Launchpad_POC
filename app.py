import streamlit as st
from utils.document_loader import load_documents
from utils.chunking import split_documents
from utils.rag_chain import create_rag_chain

st.set_page_config(page_title="Company Policy Q&A Bot")
st.title("📄 Company Policy Q&A Bot")

# this is for Load all documents ONCE 

if "documents" not in st.session_state:
    st.session_state.documents = load_documents("policydata")

documents = st.session_state.documents

query = st.text_input("Ask a policy question:")

if query:
    q = query.lower()

   
    # DETERMINISTIC POLICY ROUTING (KEY FIX)
   
    if "leave" in q:
        filtered_docs = [d for d in documents if "leave" in d.metadata["policy_type"]]

    elif "work from home" in q or "wfh" in q or "office" in q or "remote" in q:
        filtered_docs = [d for d in documents if "work" in d.metadata["policy_type"]]

    elif "expense" in q or "reimbursement" in q:
        filtered_docs = [d for d in documents if "expense" in d.metadata["policy_type"]]

    else:
        filtered_docs = []

    
    # this for handling OUT-OF-CONTEXT HANDLING
   
    if not filtered_docs:
        st.warning("I could not find this information in the provided documents.")
    else:
        chunks = split_documents(filtered_docs)
        qa_chain = create_rag_chain(chunks)

        result = qa_chain(query)

        st.success("Answer:")
        st.write(result.get("result", ""))

        st.markdown("### 📄 Source:")
        #st.write(result["source_documents"][0].metadata.get("source", "Unknown"))
        sources = result.get("source_documents", [])
        if sources:
            st.write(sources[0].metadata.get("source", "Unknown"))
        else:
            st.write("No source document found")