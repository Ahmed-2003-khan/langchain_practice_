from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a twitter post about {topic} under 20 words',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Write a linkedin post about {topic} under 20 words',
    input_variables=['topic']
)

parser = StrOutputParser()

model = ChatOpenAI()

chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
}
)

result = chain.invoke({'topic':'AI'})

print(result)

print("--"*50)

print(result['tweet'])

print("--"*50)

print(result['linkedin'])




