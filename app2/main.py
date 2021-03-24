from fastapi import FastAPI

app = FastAPI()


SERVICE_NAME = 'app2'


@app.get(f"/{SERVICE_NAME}/")
def read_root():
    return {"Hello": "app2"}
