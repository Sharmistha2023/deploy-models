# Import and deploy-models
## Import and Deploy a Model & Prediction:
  ## Sklearn:
    model:
      - d3x models import sklearn-model sklearn sklearn/model/model.joblib
    Deploy:
      - Go to sklearn directory
      - d3x serve create -n <deployment-name> -r mlflow --model <model-name> --model_version 1 --depfilepath sklearn_titanic_serve.deploy
    Prediction:
      - python client/sklearn_titanic_client.py <profile-name> <deployment-name> client/test_file/test.csv
 ## Tensorflow:
    model:
      - d3x models import tensorflow-model12 tensorflow model/model.keras
    Deploy:
      -  Go to tensorflow folder
      - d3x serve create -n <deployment-name> -r mlflow --model <model-name> --model_version 1 --depfilepath tensorflow_mnist_serve.deploy
    Prediction:
      - python client/tensorflow_mnist_client.py <profile-name> <deployment-name> client/images/3.png
 ## Xgboost:
    model:
      -  d3x models import xgboost-model xgboost xgboost/model/xgboost_titanic_model.model
    Deploy:
      - Goto xgboost directory
      - d3x serve create -n <deployment-name> -r mlflow --model <model-name> --model_version 1 --depfilepath xgboost_titanic_serve.deploy
    Prediction:
      - python client/xgboost_titanic_client.py <profile-name> <deployment-name> client/test_file/test.csv
  ## Pytorch:
    model:
      -  d3x models import pytorch-model pytorch pytorch/model/model.pt --class_path pytorch/model/sample.py --class_instance model
    Deploy:
      -  Goto pytorch directory
      - d3x serve create -n <deployment-name> -r mlflow --model <model-name> --model_version 1 --depfilepath pytorch_mnist_serve.deploy
    Prediction:
      - python client/tensorflow_mnist_client.py <profile-name> <deployment-name> client/images/3.png
  ## Custom-model:
    model:
      d3x models import custom-model custom_model custom_model/model/
    Deploy:
      -Go to custom_model directory
      - d3x serve create -n <deployment-name> -r mlflow --model <model-name> --model_version 1 --depfilepath custom_mnist_serve.deploy
    Prediction:
      - python client/tensorflow_mnist_client.py <profile-name> <deployment-name> client/images/3.png
  
