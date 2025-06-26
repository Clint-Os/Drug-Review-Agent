from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Dummy LLM class
def dummy_response(query: str) -> str:
    # Mock output simulating real LLM - to be replaced later
    # with actual model logic
    return f"(Mocked answer) You asked: '{query}'. This is a placeholder response until your model is reconnected."

# Input model
class QueryInput(BaseModel):
    query: str

# FastAPI endpoint
@app.post("/query")
async def query_endpoint(input: QueryInput):
    response = dummy_response(input.query)
    return {"result": response}


