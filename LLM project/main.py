import streamlit as st
from langchain_code import create_vector_db, get_q_a
st.title("Let me help you😎")
btn = st.button("create knowledge")
if btn:
    create_vector_db()

question = st.text_input("Ask me anything...")

if question:
    chain = get_q_a()
    response = chain(question)
    st.header("Answer :")
    st.write(response["result"])