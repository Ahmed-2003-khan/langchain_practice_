# Import ChatOpenAI - LangChain's wrapper for OpenAI's chat models
from langchain_openai import ChatOpenAI
# Import PromptTemplate - creates reusable prompt structures with variables
from langchain_core.prompts import PromptTemplate
# Import StrOutputParser - converts LLM output to plain string format
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
# Import RunnableSequence - chains multiple components in sequential execution
from langchain.schema.runnable import RunnableSequence

load_dotenv()

# PromptTemplate defines a template with placeholders for dynamic input
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

# ChatOpenAI initializes the language model for text generation
model = ChatOpenAI()

# StrOutputParser extracts clean text from the model's response object
parser = StrOutputParser()

# Second PromptTemplate takes the output from the first chain as input
prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

# RunnableSequence chains components: prompt1 -> model -> parser -> prompt2 -> model -> parser
# Data flows through each step, with outputs becoming inputs for the next component
chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

# invoke() executes the entire chain with the provided input dictionary
print(chain.invoke({'topic':'AI'}))