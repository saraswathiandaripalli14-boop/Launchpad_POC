from langchain_text_splitters import RecursiveCharacterTextSplitter
def split_documents(documents):
    #7th large policy text--->into chunks and store in memory as chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    return splitter.split_documents(documents)