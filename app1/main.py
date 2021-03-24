import os

from fastapi import FastAPI

name = os.getenv("TEST", "World")

app = FastAPI()
SERVICE_NAME = 'app1'


@app.get(f"/{SERVICE_NAME}/")
def read_root():
    return {"Hello": name}
