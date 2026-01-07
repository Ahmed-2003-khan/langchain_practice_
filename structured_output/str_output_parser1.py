# This script demonstrates how to use the StrOutputParser to chain multiple LLM calls together.
# By using a parser, we can automatically extract the text content from the LLM's response
# and pass it directly into the next prompt template without manual data handling.

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

# Initialize environment variables from a .env file (used for API keys)
load_dotenv()

# Initialize the Large Language Model (LLM)
llm = ChatOpenAI()

# Define the first prompt template: It takes a 'topic' and asks for a full report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}', 
    input_variables=['topic']
)

# Define the second prompt template: It takes the 'text' (from the first LLM output)
# and asks for a concise 5-line summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text: \n {text}',
    input_variables=['text']
)

# Initialize the StrOutputParser
# This component is crucial because LLMs return 'AIMessage' objects. 
# The parser extracts just the '.content' string so the next template can read it easily.
parser = StrOutputParser()

# Constructing the chain using LangChain Expression Language (LCEL)
# Step-by-step flow:
# 1. Fill template1 with the initial input.
# 2. Pass the prompt to the LLM.
# 3. Parse the LLM's AIMessage into a clean string using StrOutputParser.
# 4. Pass that string as the 'text' variable into template2.
# 5. Pass the new prompt to the LLM again.
# 6. Parse the final result into a string for the final output.
chain = template1 | llm | parser | template2 | llm | parser

# Invoke the chain
# Without the parser, we would have to manually extract 'result.content' 
# after the first LLM call before passing it to the second prompt.
result = chain.invoke({'topic': 'black hole'})

# Print the final 5-line summary
print(result)