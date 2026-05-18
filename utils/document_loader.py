from langchain_community.document_loaders import TextLoader
import os

def load_documents(data_path="policydata"):
    documents = []

    for file in os.listdir(data_path):
        if file.endswith(".txt"):
            #3rd this line execute loads text using TextLoader 
            # and create Langchain documents Object 
            loader = TextLoader(os.path.join(data_path, file))
            docs = loader.load()
        #4th all policy documents are loaded into memory /it is for routing 
            for d in docs:
                d.metadata["policy_type"] = file.lower()   
                d.metadata["source"] = file              

            documents.extend(docs)

    return documents





















'''from langchain_community.document_loaders import TextLoader

# add this for pdf 
#from langchain_community.document_loaders import PyPDFLoader
import os

def load_documents(data_path="PolicyData"):
    documents = []

    for file in os.listdir(data_path):
        if file.endswith(".txt"):
        #for pdf we are changing here
        #if file.endswith(".pdf"):
            loader = TextLoader(os.path.join(data_path, file))
            #for pdf we need to chnage here
            #loader = PyPDFLoader(os.path.join(data_path, file))
            docs = loader.load()

            for d in docs:
                d.metadata["policy_type"] = file.lower()
                d.metadata["source"] = file

            documents.extend(docs)

    return documents'''

'''from langchain_community.document_loaders import TextLoader
import os

def load_documents(data_path="PolicyData"):
    documents = []

    for file in os.listdir(data_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(data_path, file))
            docs = loader.load()

            for d in docs:
                d.metadata["policy_type"] = file.lower() 
                d.metadata["source"] = file

            documents.extend(docs)

    return documents '''












#it is working code 
'''from langchain_community.document_loaders import TextLoader
import os

def load_documents(data_path="policydata"):
    documents = []
    for file in os.listdir(data_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(data_path, file))
            docs = loader.load()
            documents.extend(docs)
    return documents'''