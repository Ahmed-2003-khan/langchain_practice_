from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful {domain} expert."),
    ('human', "Please explain the concept of {concept} in simple terms in 20 words.")
])

prompt = chat_template.invoke({
    "domain": "physics",
    "concept": "quantum entanglement"
})

print(prompt)  # This will print the filled messages with the provided variables