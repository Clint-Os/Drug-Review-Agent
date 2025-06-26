from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.post("/query")
async def query_endpoint(input: QueryInput):
    # Placeholder response (you’ll integrate LangChain or your logic later)
    return {"result": f"You asked about: {input.query}"}
