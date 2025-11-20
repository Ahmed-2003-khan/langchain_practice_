from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


# Chat template
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', '{query}')
])

chat_history = []
# Load Chat history
with open('chat_history.txt', 'r') as file:
    chat_history.extend(file.readlines())

# Create prompt
prompt = chat_template.invoke(
    {
        'chat_history': chat_history,
        'query': "Where is my refund?"
    }
)

