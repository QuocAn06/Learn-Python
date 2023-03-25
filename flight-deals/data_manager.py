import requests
# from pprint import pprint

SHEETY_TOKEN = "TodayIs25Mar2023"

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/43f0a7eb357595513b77fb2a238ae284/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        bearer_headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}"
        }

        response = requests.get(
            url=SHEETY_PRICES_ENDPOINT,
            headers=bearer_headers
        )

        data = response.json()
        self.destination_data = data["prices"]

        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data["prices"])

        return self.destination_data
