# Use a base image
FROM python:3.9-slim

# Install dependencies

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

COPY drug_reviews_db ./drug_reviews_db 

# avoid file watching errors
RUN mkdir -p ~/.streamlit && echo "\
[server]\n\
headless = true\n\
runOnSave = false\n\
fileWatcherType = \"none\"\n\
" > ~/.streamlit/config.toml

# Run FastAPI + Streamlit using start.sh
CMD ["./start.sh"]


