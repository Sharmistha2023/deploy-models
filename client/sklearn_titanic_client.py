# Usage: python sklearn_titanic_client.py <profile> <name> <csv_file_path>
# Ex: python sklearn_titanic_client.py dkubex sklearn-model test.csv
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
    param3 = sys.argv[3]
else:
    print("Please provide uuid & csv file path.")
    exit(1)

# Read csv File
data = open(FILE_PATH, 'rb').read()

# serving request
headers={'Authorization': SERVING_TOKEN}
resp = requests.post(SERVING_ENDPOINT, data=data, headers=headers, verify=False)
print (resp.json())
