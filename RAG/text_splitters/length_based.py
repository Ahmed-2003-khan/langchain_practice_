from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

 
loader = PyPDFLoader("RAG\\text_splitters\\dl-curriculum.pdf")
doc = loader.load()


splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)


docs = splitter.split_documents(doc)

print(docs[0].page_content)