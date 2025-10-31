import os
from fastapi import FastAPI
from pydantic import BaseModel

class Request(BaseModel):
    Prompt : str
    Language : str

app = FastAPI()

@app.post("/Plan")
def root(lang:Request):
    return (f"Planning solution for {lang.Language}")

# @app.get("/Plan?Language=cpp")