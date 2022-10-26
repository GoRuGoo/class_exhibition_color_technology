import base64

import cv2
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from functions.add_alpha_channel import add_alpha_channel_255
from functions.convert_green_to_black import convert_green_to_black
from functions.transparent_black_ground import transparent_black_ground

from fastapi import FastAPI, Form

app = FastAPI()
templates = Jinja2Templates(directory="../templates")
app.mount("/static", StaticFiles(directory="../static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/test/")
async def test(img: str = Form(...)):
    image_binary = base64.b64decode(img)
    png = np.frombuffer(image_binary, dtype=np.uint8)
    after_convert_bin_to_image = cv2.imdecode(png, cv2.IMREAD_COLOR)
    after_convert_green_to_black = convert_green_to_black(after_convert_bin_to_image)
    after_convert_green_to_black = add_alpha_channel_255(after_convert_green_to_black)
    transparent_image = transparent_black_ground(after_convert_green_to_black)
    cv2.imwrite("test.png", transparent_image)
    return_image = ndarray_to_base64(transparent_image)
    return return_image


def ndarray_to_base64(dst: np.ndarray) -> base64:
    """Numpy配列をbase64配列に変換する。
    Args:
        dst(_type_):画像のNumpy配列
    Return:
        _type_:base64文字列
    """
    result, dst_data = cv2.imencode(".png", dst)
    dst_base64 = base64.b64encode(dst_data)
    return dst_base64
