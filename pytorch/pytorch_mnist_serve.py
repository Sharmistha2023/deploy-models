import mlflow.pytorch
from ray import serve
import os
import logging
import torch

from io import BytesIO
from PIL import Image
from starlette.requests import Request
from typing import Dict

import pandas as pd
import numpy as np
from io import StringIO
import pickle
import cv2
import base64

img_w = 28
img_h = 28

# def b64_filewriter(filename, content):
#     string = content.encode('utf8')
#     b64_decode = base64.decodebytes(string)
#     fp = open(filename, "wb")
#     fp.write(b64_decode)
#     fp.close()

@serve.deployment
class ImageModel:
    def __init__(self):
        # self.model = mlflow.pytorch.jit.load(os.environ["MODEL_PATH"])
        # self.logger = logging.getLogger("ray.serve")
        self.model = mlflow.pytorch.load_model(os.environ["MODEL_PATH"])
        self.logger = logging.getLogger("ray.serve")

    async def __call__(self, starlette_request: Request) -> Dict:
        try:
            # Receive raw binary data
            image_payload_bytes = await starlette_request.body()
            self.logger.info(f"[1/2] Image payload received: {len(image_payload_bytes)} bytes")

            # Convert bytes to a NumPy array
            nparr = np.frombuffer(image_payload_bytes, np.uint8)

            # Decode the image
            img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
            if img is None:
                raise ValueError("Failed to decode image. Ensure a valid image is sent.")

            # Preprocess the image
            img = cv2.resize(img, (28, 28))
            img = img.reshape(1, 1, 28, 28)
            img = img.astype("float32") / 255.0  # Normalize pixel values

            # Perform prediction
            with torch.no_grad():
                prediction = self.model(torch.tensor(img))
                predicted_digit = np.argmax(prediction.numpy()[0])

            self.logger.info(f"[2/2] Predicted digit: {predicted_digit}")
            return {"Predicted digit": int(predicted_digit)}

        except Exception as e:
            self.logger.error(f"Request failed: {e}")
            return {"error": str(e)}, 500

deploy = ImageModel.bind()
