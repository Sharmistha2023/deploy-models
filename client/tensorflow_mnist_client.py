# Usage: python tensorflow_mnist_client.py <profile> <name> <image path>
# Ex: python tensorflow_mnist_client.py dkubex tensorflow-model images/pull-over.png
import configparser
import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

config = configparser.ConfigParser()


# Check if a parameter is provided
if len(sys.argv) > 2:
    SERVING_TOKEN = sys.argv[1]
    SERVING_ENDPOINT = sys.argv[2]
    IMAGE_PATH = sys.argv[3]
else:
    print("Please provide profile, deployment-name & image path.")
    exit(1)

# convert image to bytes
with open(IMAGE_PATH, "rb") as image:
   f = image.read()
   image_bytes = bytearray(f)

# serving request
headers={'Authorization': SERVING_TOKEN}
resp = requests.post(SERVING_ENDPOINT, data=image_bytes, headers=headers, verify=False)
print (resp.json())

