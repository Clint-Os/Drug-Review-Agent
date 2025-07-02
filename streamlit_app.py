import streamlit as st
import requests
import os

st.set_page_config(page_title="Drug Review Agent 💊")

st.title("💊 Drug Review Agent")
st.markdown("Search for a drug or condition to see relevant side effects and reviews.")

query = st.text_input("Enter a drug or condition:")

# Use HF-provided API URL or fallback to local
API_URL = os.getenv("API_URL", "/")

if st.button("Search"):
    if query.strip():
        try:
            response = requests.post(f"{API_URL.rstrip('/')}/query", json={"query": query})
            if response.status_code == 200:
                result = response.json().get("result", "No relevant results found.")
                st.success(result)
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Request failed: {e}")

