import streamlit as st
import requests

API = "http://localhost:8000"

st.title("AI News Assistant")

query = st.text_input("Ask about the news")

if st.button("Ask"):

    r = requests.get(f"{API}/ask", params={"query": query})

    st.write(r.json()["answer"])