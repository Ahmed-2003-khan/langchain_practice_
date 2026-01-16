from langchain.text_splitter import CharacterTextSplitter

# CharacterTextSplitter breaks down long text into smaller, manageable chunks based on character count
# This is a fundamental step in Retrieval-Augmented Generation (RAG) to fit context windows
splitter = CharacterTextSplitter(
    chunk_size=100, # The maximum number of characters allowed in each chunk
    chunk_overlap=0, # The number of characters that should overlap between consecutive chunks to maintain context
    separator="" # The character string used to determine where to split the text (empty string splits by length)
)

text = """
The evolution of robotics represents one of the most significant technological leaps in human history. From the early conceptualizations of mechanical servants in ancient myths to the sophisticated autonomous systems of today, robots have fundamentally altered how we interact with the physical world. Initially, robots were primarily confined to the heavy industry sector, performing repetitive and dangerous tasks on assembly lines. The first programmable robot, Unimate, revolutionized the automotive industry in the 1960s, setting the stage for a future where machines would handle the "three Ds": tasks that are dull, dirty, or dangerous.

As technology progressed, the definition of a robot expanded. Modern robotics is a multidisciplinary field that merges mechanical engineering, electronics, and computer science. The integration of Artificial Intelligence (AI) has been a game-changer

"""

# The split_text method processes the input string and returns a list of chunked strings
result = splitter.split_text(text)

print(result)
