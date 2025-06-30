from fastapi import FastAPI
from pydantic import BaseModel
from healthcheck import router as health_router
from fastapi.middleware.cors import CORSMiddleware

from vector import retriever # Import the retriever from vector.py

app = FastAPI()
app.include_router(health_router, prefix="/health", tags=["Health Check"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# Input model
class QueryInput(BaseModel):
    query: str


@app.post("/query")
async def query_endpoint(input: QueryInput):
    try:
        docs = retriever.invoke(input.query)
        result = [
            {
                "content": doc.page_content,
                "metadata": doc.metadata
            } for doc in docs
        ]
    except Exception as e:
        result = f"Error retrieving documents: {str(e)}"

    return {"results": result} 


