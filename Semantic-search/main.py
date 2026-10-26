from fastapi import FastAPI
from pydantic import BaseModel
from app.pipeline import add_sample_documents, search_documents

app = FastAPI(title="Semantic search Engine API")

@app.on_event("startup")
def startup_event():
    add_sample_documents()

class QueryRequest(BaseModel):
    query_text: str
    n_results: int = 2

@app.post("/search")
def search_endpoint(request: QueryRequest):
    results = search_documents(request.query_text, request.n_results)
    return {"results": results}
