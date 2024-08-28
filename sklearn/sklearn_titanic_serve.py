from ray import serve
import os
import logging
import json
from io import BytesIO
from PIL import Image
from starlette.requests import Request
from typing import Dict
import pandas as pd
from io import StringIO
import pickle
from sklearn import preprocessing

@serve.deployment
class TitanicModel:
    def __init__(self):
        self.model = pickle.load(open(os.environ["MODEL_PATH"]+'/model.pkl','rb'))
        self.logger = logging.getLogger("ray.serve")

    async def __call__(self, starlette_request: Request) -> Dict:
        # Get the JSON data from the request body
        data = await starlette_request.json()
        self.logger.info("[1/3] Received JSON data: {}".format(data))

        # Convert JSON to the expected format (if necessary)
        # In this case, 'data' should already be a list of lists.
        if isinstance(data, list) and all(isinstance(i, list) for i in data):
            values = self.model.predict(data)
        else:
            self.logger.error("Invalid data format received")
            return {"error": "Invalid data format"}

        self.logger.info("[2/3] Predicted values from Model: {}".format(values))
        prediction = ["setosa" if pred == 0 else "versicolor" if pred == 1 else "virginica" for pred in values]
        self.logger.info("[3/3] Inference done!")
        return {"Predicted Output:": prediction}

deploy = TitanicModel.bind()
