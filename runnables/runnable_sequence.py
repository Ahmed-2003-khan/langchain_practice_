from langchain_openai import ChatOpenAI # Wrapper for interacting with OpenAI's Chat models
from langchain_core.prompts import PromptTemplate # Template for creating structured and dynamic prompts
from langchain_core.output_parsers import StrOutputParser # Component to convert LLM output messages into raw strings
from langchain.schema.runnable import RunnableSequence # The core LCEL orchestrator that chains components into a executable sequence
from dotenv import load_dotenv

# Initialize environment variables to manage sensitive API keys and configurations
load_dotenv()


