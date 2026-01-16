from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# PyPDFLoader is a document loader that parses PDF files into LangChain Document objects
# Each page in the PDF becomes a separate Document object with page_content and metadata
loader = PyPDFLoader("RAG\\text_splitters\\dl-curriculum.pdf")
doc = loader.load()

# CharacterTextSplitter breaks down Document objects into smaller chunks based on character count
# This is used to ensure text fits within LLM context limits or to optimize retrieval
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)

# split_documents applies the splitting logic to already loaded LangChain Document objects
# It preserves metadata from the original documents while chunking the content
docs = splitter.split_documents(doc)

print(docs[0].page_content)