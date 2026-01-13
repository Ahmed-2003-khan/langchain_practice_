from langchain_community.document_loaders import TextLoader

loader = TextLoader('RAG\document_loaders\glue.txt', encoding='utf-8')

docs = loader.load()

print(docs)

