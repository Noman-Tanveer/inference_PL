import os
from typing import Union
from PIL import Image, ImageDraw

from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from io import BytesIO
from fastapi.responses import Response

from app.api.dependencies.detect import detect_v5
from app.api.dependencies.generate import create_image

from fastapi import applications
from fastapi.openapi.docs import get_swagger_ui_html


def swagger_monkey_patch(*args, **kwargs):
    """
    Wrap the function which is generating the HTML for the /docs endpoint and
    overwrite the default values for the swagger js and css.
    """
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.29/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.29/swagger-ui.css")


# Actual monkey patch
applications.get_swagger_ui_html = swagger_monkey_patch

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

class Item(BaseModel):
    text: str

@app.post("/generate-image/")
async def generate_image(prompt: Item):
    # Create an image based on the received text
    img = create_image(prompt.text)
    draw = ImageDraw.Draw(img)

    # Convert the PIL image to bytes
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")
    img_bytes = img_buffer.getvalue()

    # Create a FastAPI response with the image bytes and content type
    return Response(content=img_bytes, media_type="image/png")


@app.post("/detect/")
async def detect_image(image_bytes: bytes = File()):
    # Call the detect function
    processed_image_bytes = detect_v5(image_bytes)

    # Return the processed image as bytes
    return StreamingResponse(BytesIO(processed_image_bytes), media_type="image/jpeg")
