from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda

from dotenv import load_dotenv

load_dotenv()

# Custom function to count words in the generated joke
# This demonstrates how to integrate arbitrary Python functions into LCEL chains
def word_count(text):
    return len(text.split())

# Prompt template for joke generation
prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

# ChatOpenAI model instance
model = ChatOpenAI()

# Output parser to convert AIMessage to string
parser = StrOutputParser()

# First chain: generates a joke string from the topic
joke_gen_chain = RunnableSequence(prompt, model, parser)

# RunnableLambda wraps custom Python functions to make them compatible with LCEL
# This allows seamless integration of custom logic into the chain
# The parallel chain outputs both the joke and its word count simultaneously
parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'word_count': RunnableLambda(word_count)
    }
)

# Complete pipeline: generate joke → parallel processing (preserve joke + count words)
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# Execute the chain with a topic input
print(final_chain.invoke({'topic': 'AI'}))
