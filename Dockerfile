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

# Streamlit config (disable telemetry, set safe port & dir)
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

# Forces Streamlit to use this config path (no / root access)
ENV STREAMLIT_CONFIG_DIR=/app/.streamlit
ENV XDG_CONFIG_HOME=/app

# Expose ports
EXPOSE 8501
EXPOSE 8000

# Start app
CMD ["bash", "start.sh"]
 





