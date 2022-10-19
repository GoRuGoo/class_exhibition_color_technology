from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}
