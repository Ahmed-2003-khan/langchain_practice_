from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
# The Evolution of Artificial Intelligence in Software Engineering

## Introduction
Artificial Intelligence (AI) has transitioned from a theoretical concept in academic papers to a cornerstone of modern software engineering. As developers, we are witnessing a paradigm shift where code is no longer just written; it is generated, optimized, and maintained with the assistance of intelligent agents. This evolution is not merely about automation but about augmenting human creativity and problem-solving capabilities. In the current landscape, understanding the integration of AI is no longer optional for software professionals.

## The Historical Context
The roots of AI can be traced back to the mid-20th century, with pioneers like Alan Turing and John McCarthy laying the groundwork. Early AI systems were rule-based, relying on complex sets of "if-then" statements to simulate

"""

# RecursiveCharacterTextSplitter is the recommended splitter for generic text.
# It tries to split on a list of characters (like \n\n, \n, " ") in order until chunks are small enough.
# This helps keep related pieces of text (like paragraphs or sentences) together.
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, # Targeted maximum size of each chunk
    chunk_overlap=0, # No overlap between chunks in this example
    
)

# split_text takes a string and returns a list of smaller strings based on the splitting logic
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])