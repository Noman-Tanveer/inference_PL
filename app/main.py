import os
from typing import Union

from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import io
import cv2
import numpy as np

from app.api.dependencies.detect import detect_v5

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/detect/")
async def detect_image(image_bytes: bytes = File()):
    # Call the detect function
    processed_image_bytes = detect_v5(image_bytes)

    # Return the processed image as bytes
    return StreamingResponse(io.BytesIO(processed_image_bytes), media_type="image/jpeg")
