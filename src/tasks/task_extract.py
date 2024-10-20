import csv
from prefect import task
from config import config
import requests
from .utils import handle_invalid_ruc


@task(name="2. Extraer info de csv")
def task_extract_csv(filename):
  data = []
  with open(filename, "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
      tmp_data = (row["ruc"], row["condicion"])
      data.append(tmp_data)
  
  return data

@task(name="4. Extraer data de ruc")
def task_extract_ruc(ruc):
  token = config.API_TOKEN
  headers = {
    "Authorization" : "Bearer " + token,
    "Content-Type" : "application/json"
  }

  data = {
    "ruc" : ruc
  }
  url_ruc = config.ENDPOINTS["ruc"]
  response = requests.post(url_ruc, json=data, headers=headers)

  if response.status_code == 200:
    if response.json()["success"]:
      data = response.json()["data"]
      nombre_o_razon_social = data["nombre_o_razon_social"]
      estado = data["estado"]
      return (nombre_o_razon_social, estado)
    else:
      handle_invalid_ruc(ruc)
  
  else:
    print("error: ", response.status_code)