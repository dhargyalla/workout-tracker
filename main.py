import requests
from datetime import datetime
import os

nutrients_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoints = os.environ["SHEET_ENDPOINT"]

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]
TOKEN = os.environ["MY_TOKEN"]


GENDER = "male"
WEIGHT_KG = 76
HEIGHT_CM = 170
AGE = 34

query_text = input("Tell me which exercises you did: ")

nutrients_params = {
    "query": query_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": f"Bearer{TOKEN}"
}

response = requests.post(url=nutrients_endpoint, json=nutrients_params, headers=headers)
result = response.json()
print(result['exercises'])
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for item in result['exercises']:
    exercise = item['name'].title()
    duration = item['duration_min']
    calories = item['nf_calories']
    excel_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }
    print('Test')
    print(excel_params)

    excel_request = requests.post(url=sheety_endpoints, json=excel_params)
    data = excel_request.json()
    print(data)

    # print(excel_request.text)
