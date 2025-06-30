import streamlit as st
import requests

st.title("💊 Drug Review Agent")

query = st.text_input("Enter a drug or condition:")

if st.button("Search"):
    if query:
        try:
            response = requests.post("http://localhost:8000/query", json={"query": query})
            if response.status_code == 200:
                st.success(response.json().get("result", "No result found"))
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")
