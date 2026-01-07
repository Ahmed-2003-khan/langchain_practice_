# This script demonstrates the use of JsonOutputParser to get structured data from an LLM.
# Unlike the string parser, this parser instructs the LLM to return a JSON object,
# which LangChain then automatically converts into a Python Dictionary.

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# Load environment variables (API keys)
load_dotenv()

# Step 1: Initialize the HuggingFace Model
# We use HuggingFaceEndpoint to connect to the model hosted on HuggingFace servers.
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

# Wrap the endpoint in ChatHuggingFace to make it compatible with Chat Message logic
model = ChatHuggingFace(llm=llm)

# Step 2: Initialize the JSON Output Parser
# This parser has two jobs:
# 1. Provide instructions to the LLM on how to format the JSON.
# 2. Convert the resulting string back into a Python Dictionary.
parser = JsonOutputParser()

# Step 3: Define the Prompt Template
# Note the use of {format_instruction}. This is where the parser's specific
# formatting rules will be injected into the prompt.
template = PromptTemplate(
    template='Give me the name, age, city of a fictional person \n {format_instruction}',
    input_variables=[],
    # partial_variables allows us to pre-fill the format instructions 
    # so we don't have to pass them manually during every invoke() call.
    partial_variables={
        'format_instruction': parser.get_format_instructions()
    }
)

# Step 4: Create the Chain
# Flow: Prompt -> Model (returns text) -> Parser (returns Python Dict)
chain = template | model | parser

# Invoke the chain with an empty dictionary because no 'topic' or 'input' is required here.
result = chain.invoke({})

# Step 5: Output the result
# 'result' is now a real Python dictionary, not just a string!
print(result)

# Verify the type to confirm it is a <class 'dict'>
print(type(result))

# NOTE ON LIMITATION:
# As you mentioned, JsonOutputParser is "loose." It asks for JSON but doesn't 
# strictly force the model to follow a specific structure (like ensuring 'age' is an integer).
# For strict structure enforcement, we would move to StructuredOutputParser or PydanticOutputParser.