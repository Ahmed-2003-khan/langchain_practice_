from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel

from dotenv import load_dotenv

load_dotenv()

# First prompt generates a joke based on the input topic
prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

# ChatOpenAI instance to process prompts and generate responses
model = ChatOpenAI()

# Parser to extract string content from model responses
parser = StrOutputParser()

# Second prompt takes the generated joke and creates an explanation
prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

# First chain: generates a joke from the topic input
joke_gen_chain = RunnableSequence(prompt1, model, parser)

# RunnableParallel executes multiple runnables concurrently on the same input
# RunnablePassthrough forwards the input unchanged, preserving the original joke
# This creates a dict with both the joke and its explanation
parallel_chain = RunnableParallel(
    {
        'joke': RunnablePassthrough(),
        'explanation': RunnableSequence(prompt2, model, parser)
    }
)

# Final chain: generates joke, then creates parallel outputs (joke + explanation)
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

# Invoke the complete pipeline with a topic
print(final_chain.invoke({'topic':'AI'}))