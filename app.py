import os

from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/name")
def read_root():
    return {"name": "shani blau"}


@app.post("/uploadfile")
async def create_upload_file(file: UploadFile):
    name = file.filename
    if not os.path.exists("../dogs"):
        os.mkdir("../dogs")
    with open(f"../dogs/{name}", 'wb') as file:
        file.read()
    return {"filename": name}
