import configparser
import requests
import sys
import urllib3
import pandas as pd
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

config = configparser.ConfigParser()

# Check if a parameter is provided
if len(sys.argv) > 2:
    SERVING_TOKEN = sys.argv[1]
    SERVING_ENDPOINT = sys.argv[2]
    csv_file_path = sys.argv[3]
else:
    print("Please provide uuid & csv file path.")
    exit(1)

# Read CSV file
try:
    df = pd.read_csv(csv_file_path, header=None)  # Use header=None if your CSV doesn't have headers
except Exception as e:
    print(f"Error reading CSV file: {e}")
    exit(1)

# Convert DataFrame to list of lists
data = df.values.tolist()
# Convert data to JSON format
data_json = json.dumps(data)

# Serving request
headers = {'Authorization': SERVING_TOKEN, 'Content-Type': 'application/json'}
try:
    resp = requests.post(SERVING_ENDPOINT, data=data_json, headers=headers, verify=False)
    print(f"Response JSON: {resp.json()}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

