# Use an official Python image
FROM python:3.11-slim

# Create a non-root user
RUN adduser --disabled-password --no-create-home --gecos '' appuser

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create Streamlit config directory with correct permissions
RUN mkdir -p /app/.streamlit && \
    echo "\
[server]\n\
headless = true\n\
port = 8501\n\
enableCORS = false\n\
\n\
[browser]\n\
gatherUsageStats = false\n\
" > /app/.streamlit/config.toml

# Set environment variable for Streamlit config
ENV STREAMLIT_HOME=/app/.streamlit
ENV XDG_CONFIG_HOME=/app

ENV API_URL=http://localhost:8000 


# Change ownership to non-root user
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose ports
EXPOSE 8501
EXPOSE 8000

# Start the app
CMD ["bash", "start.sh"]


 





