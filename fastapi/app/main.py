import base64

import cv2
import numpy as np
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from functions.add_alpha_channel import add_alpha_channel_255
from functions.convert_green_to_black import convert_green_to_black
from functions.make_visualization_graph import make_visualization_graph
from functions.transparent_black_ground import transparent_black_ground

from fastapi import FastAPI, Form, Request

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


@app.get("/")
async def mainpage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/transparent/")
async def test(
    img: str = Form(...),
    min_hue: int = Form(...),
    max_hue: int = Form(...),
    min_sat: int = Form(...),
    max_sat: int = Form(...),
    judge_mani_black: int = Form(...),
    detect_min_bright: int = Form(...),
    detect_max_bright: int = Form(...),
):
    image_binary = base64.b64decode(img)
    png = np.frombuffer(image_binary, dtype=np.uint8)
    after_convert_bin_to_image = cv2.imdecode(png, cv2.IMREAD_COLOR)
    graph_image = make_visualization_graph(after_convert_bin_to_image)
    after_convert_green_to_black = convert_green_to_black(
        after_convert_bin_to_image,
        min_hue,
        max_hue,
        min_sat,
        max_sat,
        judge_mani_black,
        detect_min_bright,
        detect_max_bright,
    )
    after_convert_green_to_black = add_alpha_channel_255(after_convert_green_to_black)
    transparent_image = transparent_black_ground(after_convert_green_to_black)
    return_image = ndarray_to_base64(transparent_image)
    return_graph_image = ndarray_to_base64(graph_image)
    return {"image": return_image, "graph": return_graph_image}


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


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True, access_log=True)
