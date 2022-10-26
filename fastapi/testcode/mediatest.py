from email.mime import base
import io
import base64
import cv2
import numpy as np
from fastapi.responses import FileResponse, StreamingResponse,JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Request, UploadFile,Form,File


app = FastAPI()
templates = Jinja2Templates(directory="../templates")
app.mount("/static", StaticFiles(directory="../static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
async def mainpage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.post("/files/")
async def file(file: bytes = File(...)):
    content = file.decode("utf-8")
    formatfile = content.split("\n")
    return {"filedetail": formatfile}


@app.post("/uploadfile/")
async def upload_file(file: UploadFile):
    bin_data = io.BytesIO(file.file.read())
    img = read_image(bin_data)
    cv2.imwrite("img.png", img)
    return "sucess"


@app.post("/mediareturn/", response_class=FileResponse)
async def mediareturn(file: UploadFile = File(...)):
    binary_data = io.BytesIO(file.file.read())
    img = read_image(binary_data)
    res, im_png = cv2.imencode(".png", img)
    return StreamingResponse(io.BytesIO(im_png.tobytes()), media_type="image/png")

@app.post("/test/")
async def test(img:str=Form(...)):
    image_binary = base64.b64decode(img)
    png = np.frombuffer(image_binary,dtype=np.uint8)
    after_convert_image = cv2.imdecode(png,cv2.IMREAD_COLOR)
    cv2.imwrite("test.png",after_convert_image)
    return img

def read_image(bin_data):
    """Read Image.

    Args:
        bin_data(_type_): binary image data
    Return:
        np.ndarray: Image
    """
    file_bytes = np.asarray(bytearray(bin_data.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    return img
