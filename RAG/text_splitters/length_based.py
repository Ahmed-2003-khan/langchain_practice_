from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

 
# PyPDFLoader parses PDF documents into LangChain Document objects (content + metadata)
loader = PyPDFLoader("RAG\\text_splitters\\dl-curriculum.pdf")
doc = loader.load()


# CharacterTextSplitter splits text based on character count and a specific separator
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)


# split_documents chunks the content of Document objects while preserving their metadata
docs = splitter.split_documents(doc)

print(docs[0].page_content)