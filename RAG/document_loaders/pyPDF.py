from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('RAG\document_loaders\dl-curriculum.pdf')
docs = loader.load()

print(len(docs))

print("=="*50)

print(docs[0].page_content)

print("=="*50)

print(docs[0].metadata)

