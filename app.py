import streamlit as st
from utils.document_loader import load_documents
from utils.chunking import split_documents
from utils.rag_chain import create_rag_chain

st.set_page_config(page_title="Company Policy Q&A Bot")
st.title("📄 Company Policy Q&A Bot")

# -------------------------------------------------
# Load all documents ONCE
# -------------------------------------------------
if "documents" not in st.session_state:
    st.session_state.documents = load_documents("PolicyData")

documents = st.session_state.documents

query = st.text_input("Ask a policy question:")

if query:
    q = query.lower()

    # -------------------------------------------------
    # ✅ DETERMINISTIC POLICY ROUTING (KEY FIX)
    # -------------------------------------------------
    if any(word in q for word in [
        "leave", "casual leave", "paid leave", "earned leave"
    ]):
        filtered_docs = [
            d for d in documents
            if "leave" in d.metadata.get("source", "").lower()
        ]

    elif any(word in q for word in [
        "work from home", "wfh", "office", "office days",
        "come to office", "hybrid", "remote"
    ]):
        filtered_docs = [
            d for d in documents
            if "wfh" in d.metadata.get("source", "").lower()
        ]

    elif any(word in q for word in [
        "expense", "reimbursement", "travel", "claim", "billing"
    ]):
        filtered_docs = [
            d for d in documents
            if "expense" in d.metadata.get("source", "").lower()
        ]

    else:
        filtered_docs = []

    # -------------------------------------------------
    # ✅ OUT-OF-CONTEXT HANDLING
    # -------------------------------------------------
    if not filtered_docs:
        st.warning("I could not find this information in the provided documents.")
    else:
        chunks = split_documents(filtered_docs)
        qa_chain = create_rag_chain(chunks)

        result = qa_chain(query)

        st.success("Answer:")
        st.write(result.get("result", ""))

        st.markdown("### 📄 Source:")
        st.write(result["source_documents"][0].metadata.get("source", "Unknown"))