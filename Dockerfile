# Use an official Python image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Streamlit config fix for Hugging Face (create writable config path)
RUN mkdir -p /app/.streamlit && \
    echo "\
[server]\n\
headless = true\n\
port = 8501\n\
enableCORS = false\n\
" > /app/.streamlit/config.toml

# Ensure Streamlit uses the writable config directory
ENV STREAMLIT_HOME=/app/.streamlit

# Expose Streamlit and FastAPI ports
EXPOSE 8501
EXPOSE 8000

# Start both FastAPI and Streamlit
CMD ["bash", "start.sh"] 





