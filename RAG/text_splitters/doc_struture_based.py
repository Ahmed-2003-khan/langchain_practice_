from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

text = """
class TextAnalyzer:
    ""
    A class to analyze text content for RAG pipelines.

    Example usage:
    >>> analyzer = TextAnalyzer("Sample text")
    >>> analyzer.get_word_count()
    2
    ""

    def __init__(self, content: str):
        self.content = content

    def get_word_count(self) -> int:
        ""Returns the number of words in the text.""
        return len(self.content.split())

    def summarize(self) -> str:
        ""Returns a brief summary of the content.""
        return f"Summary: {self.content[:50]}..."

def process_document(text: str):
    
    analyzer = TextAnalyzer(text)
    print(analyzer.summarize())

if __name__ == "__main__":
    process_document("This is a sample document for testing.")
"""
# from_language is a specialized constructor for RecursiveCharacterTextSplitter.
# It automatically pre-populates the delimiters based on the syntax of the target language (e.g., Python).
# This ensures that code blocks like classes and functions are kept together when possible.
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, # Use Python language separators (class, def, etc.)
    chunk_size=100, # Max characters per chunk
    chunk_overlap=0, # No overlap in this example
)

# split_text applies the language-aware splitting logic to the source code string
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])