from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

# PromptTemplate defines the structure of the input with placeholders for dynamic values
# The template string uses {topic} as a variable that will be replaced at runtime
prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

# ChatOpenAI creates an instance of the language model that will process the prompt
# This connects to OpenAI's API using credentials from environment variables
model = ChatOpenAI()

# StrOutputParser extracts the text content from the model's response object
# It transforms the AIMessage into a simple string for easier consumption
parser = StrOutputParser()



