from fastapi import FastAPI
from pydantic import BaseModel
from vector import retriever # Import the retriever from vector.py

app = FastAPI()

# Dummy LLM class
def dummy_response(query: str) -> str:
    # Mock output simulating real LLM - to be replaced later
    # with actual model logic
    return f"(Mocked answer) You asked: '{query}'. This is a placeholder response until your model is reconnected."

# Input model
class QueryInput(BaseModel):
    query: str


@app.post("/query")
async def query_endpoint(input: QueryInput):
    try:
        docs = retriever.invoke(input.query)
        result = "\n".join([doc.page_content for doc in docs])
    except Exception as e:
        result = f"Error retrieving documents: {str(e)}"

    return {"result": result} 


