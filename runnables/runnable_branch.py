from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel, RunnableLambda, RunnableBranch

from dotenv import load_dotenv

load_dotenv()

# First prompt generates a 100-word report on the given topic
prompt1 = PromptTemplate(
    template='Write a report on {topic} in 100 words.',
    input_variables=['topic']
)

# Second prompt summarizes text to 20 words
# This is used conditionally when the report exceeds 80 words
prompt2 = PromptTemplate(
    template='summarize the text in 20 words. \n {text}',
    input_variables=['text']
)

# ChatOpenAI model and string parser for processing
model = ChatOpenAI()
parser = StrOutputParser()

# First chain generates the initial report
report_gen_chain = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 80, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

# Complete pipeline: generate report → conditionally summarize if too long
final_chain = RunnableSequence(report_gen_chain, branch_chain)

# Execute the chain with a topic - output will be summarized only if it exceeds 80 words
print(final_chain.invoke({'topic': 'AI'}))