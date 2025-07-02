#!/bin/bash

echo "Step 1: Removing old vector DB..."
rm -rf drug_reviews_db/

echo "Step 2: Regenerating Chroma DB with vector.py..."
python vector.py

echo "Step 3: Killing any process on port 8000..."
PID=$(lsof -ti:8000)
if [ -n "$PID" ]; then
    kill -9 $PID
    echo "Killed process $PID using port 8000"
else
    echo "No process found using port 8000"
fi

echo "🚀 Step 4: Starting backend..."
./start.sh &

sleep 5  # Wait for server to start

echo "🧪 Step 5: Testing FastAPI /query endpoint..."
curl -X POST http://localhost:8000/query \
     -H "Content-Type: application/json" \
     -d '{"query": "headache after taking ibuprofen"}'

echo -e "\n Done!"
