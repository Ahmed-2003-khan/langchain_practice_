from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative:\n\n{feedback_text}\n {format_instructions}",
    input_variables=["feedback_text"],
    partial_variables={"format_instructions": parser2.get_format_instructions()},
)

classifier_chain = prompt1 | model | parser2

# print(classifier_chain.invoke({"feedback_text": "I love the new design of your website!"}))

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback. \n {feedback}',
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback. \n {feedback}',
    input_variables=["feedback"],
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model | parser),
    (lambda x:x.sentiment=='negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Unable to determine sentiment.")
)

chain = classifier_chain | branch_chain

# print(chain.invoke({"feedback_text": "I love the new design of your website!"}))

chain.get_graph().print_ascii()
