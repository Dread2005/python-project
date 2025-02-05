import requests
from datetime import datetime

GENDER = "Male"
WEIGHT_KG = 63
HEIGHT_CM = 182
AGE = 19

APP_ID = "5a6c13a7"
API_KEY = "7bf298d8cb7a78555e755d44e67f0ef9"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/0d8564c85570e0619c274a96dbec7a79/workout2/sheet1"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_header = {
        "Authorization": "Basic RHJlYWRmb3JkOjc2MTAyMDA1"
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=sheety_header)

    print(sheet_response.text)
