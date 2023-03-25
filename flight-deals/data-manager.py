import requests
from pprint import pprint

SHEETY_TOKEN = "TodayIs25Mar2023"

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/43f0a7eb357595513b77fb2a238ae284/flightDeals/prices"

bearer_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

sheety_response = requests.get(
    url=SHEETY_PRICES_ENDPOINT,
    headers=bearer_headers
)
data = sheety_response.json()
data = data['prices']

pprint(data)
