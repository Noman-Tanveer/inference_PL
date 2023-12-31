import os

import cv2
import numpy as np

import torch

model_name='yolov5s.pt'
model = torch.hub.load(os.path.join(os.getcwd(), "app/api/dependencies/yolov5"), 'custom',
                        source='local', path = model_name, force_reload = True)

def detect_v5(image_bytes: bytes) -> bytes:
    # Convert the bytes into an OpenCV Image
    input_image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    # Perform detection
    # Loading in yolov5s - you can switch to larger models such as yolov5m or yolov5l, or smaller such as yolov5n
    results = model(input_image)
    processed_image = results.render()[0]  # Placeholder

    return cv2.imencode('.jpg', processed_image)[1].tobytes()
