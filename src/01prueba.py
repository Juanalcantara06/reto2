import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("APIPERU_TOKEN")

url_ruc = "https://apiperu.dev/api/ruc"

ruc = {
  "ruc" : "10427084600"
}

headers = {
  "Authorization" : "Bearer " + token,
  "Content-Type" : "application/json"
}

response = requests.post(url_ruc, json=ruc, headers=headers)

if response.status_code == 200:
  print(response.json())
else:
  print("error: ", response.status_code)