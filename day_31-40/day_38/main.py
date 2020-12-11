import requests
from datetime import datetime
import json

with open("./day_31-40/day_38/creds.json") as f:
    creds = json.load(f)

GENDER = "male"
WEIGHT = 103
HEIGHT = 178
AGE = 28

APP_ID = creds['app_id']
API_KEY = creds['api_key']

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = creds['sheety_endpoint']

exercise_input = input("How did you exercise today: ")

exercise_params = {
 "query":exercise_input,
 "gender":GENDER,
 "weight_kg":WEIGHT,
 "height_cm":HEIGHT,
 "age":AGE
}

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

response = requests.post(url = exercise_endpoint, json = exercise_params, headers = headers)
result = response.json()

### Sheety Task ###
today_date = datetime.now().strftime("%d/%m/%Y")
timestamp = datetime.now().strftime("%X")

tokens = {
    "Authorization" : "Bearer supersecrettoken"
}

for exercise in result['exercises']:
    sheet_inputs = {
        "workout" : {
            "date" : today_date,
            "time" :timestamp,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url = sheety_endpoint, json = sheet_inputs, headers = tokens)

print(sheet_response.text)