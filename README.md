📄 Company Policy Q&A Bot (RAG POC) 

1. Overview 

This project is a Retrieval-Augmented Generation (RAG) based chatbot built using Streamlit and LangChain. 

It answers user questions only from company policy documents (Leave, Work From Home, and Expense policies). 

The bot: 

✅ Loads policy documents from text files 

✅ Splits them into chunks 

✅ Converts chunks into embeddings 

✅ Stores embeddings in a vector database (FAISS) 

✅ Retrieves the most relevant content for a user query 

✅ Uses an LLM to generate grounded answers 

❌ Does not answer questions outside the provided documents 

 

2. Supported Policies 

The current POC supports the following policies: 

-->Leave Policy (leave-policy.txt) 

leave-policy.txt 

-->Work From Home Policy (work from home-policy.txt) 

work from home-policy.txt 

-->Expense Policy (expense-policy.txt) 

expense-policy.txt 

Each policy is stored as a separate text file and routed deterministically. 

 

3. Example Questions 

----->Leave Policy 

How many casual leaves are allowed per year? 

Can unused casual leaves be carried forward? 

How many days of paternity leave are allowed? 

----->Work From Home Policy 

Explain work from home policy 

How many days should employees come to the office? 

Can employees work remotely every day? 

------>Expense Policy 

What is the daily food expense limit? 

Are receipts mandatory for expense claims? 

Within how many days should expense reports be submitted? 

------>Out-of-Context (Expected to Fail) 

Who is the CEO of the company? 

What is the company salary structure? 

 

4. Project Structure 

    RAG-POC/ 

    │ 

    ├── app.py 

    ├── requirements.txt 

    │ 

    ├── policydata/ 

    │   ├── leave-policy.txt 

    │   ├── work from home-policy.txt 

    │   └── expense-policy.txt 

    │ 

    ├── vectorstore/ 

    │   └── (FAISS index files – created at runtime if persistence is enabled) 

    │ 

     ├── utils/ 

     │   ├── __init__.py 

     │   ├── document_loader.py 

     │   ├── chunking.py 

     │   ├── rag_chain.py 

     │   └── llm_config.py 

     │ 

     └── venv/ 

 

5. Installation & Setup 

Step 1: Clone the Repository 

    1. git clone saraswathiandaripalli14-boop/Launchpad_POC 

    2. cd Launchpad-POC or RAG-POC

 

Step 2: Create and Activate Virtual Environment 

     python -m venv venv 

Windows 

     venv\Scripts\activate 

 

Step 3: Install Dependencies 

     pip install -r requirements.txt 

 

        Install python 3.10 - 3.11 only it support 

        UI Framework 

        Streamlit==1.35.0 

        LangChain Core & Integrations 

        langchain==0.2.14 langchain-community==0.2.12 langchain-openai==0.1.22 langchain-text-splitters==0.2.2 

        Vector Database 

        faiss-cpu==1.8.0 

        Environment Variable Support 

        python-dotenv==1.0.1 

        for pdf data we need to install 

        pypdf==4.2.0 



Step 4: Set OpenAI API Key 

The application requires an OpenAI-compatible API key. 

For API key open this link and create and generate API key 
first step is to login into gen engine https://generative.engine.capgemini.com/ 

Store that key for futures usgae 
past that key in the below “your_api_key_here” 

     setx OPENAI_API_KEY "your_api_key_here" 

Restart VS Code after setting the key. 

 

Step 5: Run the Application 

     streamlit run app.py 

Open the browser at: 

     http://localhost:8501 

 

6. How the RAG Pipeline Works 

Policy documents are loaded from policydata/ 

policydata/ 

Documents are split into overlapping chunks 

Chunks are embedded and stored in FAISS (in-memory or in vectorstore/ if persistence is enabled) 

vectorstore/ 

User query is routed to the correct policy 

Relevant chunks are retrieved from FAISS 

LLM generates an answer using retrieved context 

Source document is displayed 

 

7. Out-of-Context Handling 

If a question is not related to any policy document, the bot responds with: 

"I could not find this information in the provided documents." 

This prevents hallucination and ensures compliance. 

 

8. Design Decisions 

Filename-based routing for simplicity and stability 

FAISS for fast vector search 

Streamlit for quick UI development 

FakeEmbeddings for POC stability 

 

9. Future Enhancements 

PDF document support 

Upload policy files via UI 

Persistent vector store (already scaffolded via vectorstore/) 

vectorstore/ 

Semantic routing using embeddings 

Chat history support 

 

10. Conclusion 

This project demonstrates a clean, beginner-friendly RAG implementation suitable for: 

Proof of Concept (POC) 

Client demos 

Interview projects 

Internal HR policy assistants 

 

✅ Status: Working and GitHub-synced 
