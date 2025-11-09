from fastapi import FastAPI

# uvicorn src.api.api:app --reload
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hallo Welt!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "query": q}

