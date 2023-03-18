import requests

GENDER = "male"
WEIGHT_KG = 89
HEIGHT_CM = 180
AGE = 26

APP_ID = "802368ef"
APP_KEY = "2ba4900dbd7d46f2e744c7fde87ea238"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

