from fastapi import FastAPI
from db.models import User

app = FastAPI()

api_path = "/api/v1"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get(f"{api_path}/connect")
async def api():
    return {"message": "connected"}
