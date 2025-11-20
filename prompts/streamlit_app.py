from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

st.header("Research Tool with GPT-3.5 Turbo")

paper_input = st.selectbox(
    "Select a research paper:", ["Select... ", "Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox(
    "Select a writing style:", ["Select... ", "Formal", "Informal", "Technical", "Layman"])

length_input = st.selectbox(
    "Select the desired length of the summary:", ["Select... ", "Short (100 words)", "Medium (250 words)", "Long (500 words)"])

template = PromptTemplate(
    template="""
    Please summarize the research paper titled "{paper_input}" in a {style_input} style. The summary should be approximately {length_input} in length.
    """,
    input_variables=["paper_input", "style_input", "length_input"],
)

if st.button("Generate Summary"):
    chain = template | model
    result = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.write(result.content)