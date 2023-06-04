from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.get("/name")
def read_root():
    return {"name": "shani blau"}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
