import os
from typing import Union

from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import io
import cv2
import numpy as np

from app.api.dependencies.detect import detect_v5
from app.api.dependencies.generate import create_image

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/generate-image/")
async def generate_image(text: str):
    # Create an image based on the received text
    img_data = create_image(text)

    # Return the image as a response
    return {"image": img_data}

@app.get("/detect/")
async def detect_image(image_bytes: bytes = File()):
    # Call the detect function
    processed_image_bytes = detect_v5(image_bytes)

    # Return the processed image as bytes
    return StreamingResponse(io.BytesIO(processed_image_bytes), media_type="image/jpeg")
