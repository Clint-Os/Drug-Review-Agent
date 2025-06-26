# Use a base image
FROM python:3.9-slim

# Install dependencies

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Run FastAPI + Streamlit using start.sh
CMD ["./start.sh"]


