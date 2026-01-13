from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='RAG\document_loaders\directory',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))

for doc in docs:
    print(doc.page_content)

docs = loader.lazy_load()

for doc in docs:
    print(doc.page_content)

