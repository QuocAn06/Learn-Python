import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 89
HEIGHT_CM = 180
AGE = 26

APP_ID = "802368ef"
APP_KEY = "2ba4900dbd7d46f2e744c7fde87ea238"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/43f0a7eb357595513b77fb2a238ae284/workoutTracking/workouts"

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(
    url=exercise_endpoint,
    json=parameters,
    headers=headers
)

result = response.json()

today_date = datetime.now().strftime("%d%m%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_input = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers ={
        "Authorization": "Bearer asfa323d1fa5sdf135ads2f1"
    }

    sheety_response = requests.post(
        url=sheety_endpoint,
        json=sheety_input,
        headers=bearer_headers
    )

    print(sheety_response.text)
