import requests
from datetime import datetime

my_exercise = input("What did you do: ")
age = int(input("Age: "))
height = 182
weight = 65


neutritionix_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
neutritionix_nutrients_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"
neutritionix_api_key = "7bf298d8cb7a78555e755d44e67f0ef9"
neutritionix_id = "5a6c13a7"

sheety_add_endpoint = "https://api.sheety.co/0d8564c85570e0619c274a96dbec7a79/workout2/sheet1"
sheety_veiw_endpoint = "https://api.sheety.co/0d8564c85570e0619c274a96dbec7a79/workout2/sheet1"

neutritionix_header = {
    "x-app-id": neutritionix_id,
    "x-app-key": neutritionix_api_key
}

neutritionix_params = {
    "query": my_exercise,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}

neutritionix_req = requests.post(url=neutritionix_exercise_endpoint,
                                 json=neutritionix_params,
                                 headers=neutritionix_header)


neutrix_response = neutritionix_req.json()
print(neutrix_response)

date_now = datetime.now()
workout_date = date_now.strftime("%Y/%b/%a")
entry_time = date_now.strftime("%H")

for data in neutrix_response["exercises"]:
    exercise = data["user_input"]
    duration = data["duration_min"]
    calories = data["nf_calories"]

    sheety_json = {
        "sheet1": {
                "Date": workout_date,
                "Time": entry_time,
                "Exercise": exercise,
                "Duration": duration,
                "Calories": calories
        }
    }

    sheety_req = requests.post(sheety_add_endpoint, json=sheety_json)
    print(sheety_req.text)



