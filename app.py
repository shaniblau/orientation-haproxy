from fastapi import FastAPI

app = FastAPI()


@app.get("/name")
def read_root():
    return {"name": "shani blau"}

