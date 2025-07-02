#!/bin/bash

# Start FastAPI (api.py) in the background
uvicorn api:app --host 0.0.0.0 --port 8000 &

# Start Streamlit frontend 
streamlit run streamlit_app.py --server.port 8501 --server.address=0.0.0.0
