from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template='Detect whether it is AI or human written just write one word AI or human\n {text}',
    input_variables=['text']
)

loader = TextLoader('RAG\document_loaders\glue.txt', encoding='utf-8')

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'text': docs[0].page_content}))


