import requests
from datetime import datetime
import smtplib
import time

# ---------------------------- CONSTANTS ------------------------------- #
MY_EMAIL = "sorry8699@gmail.com"
MY_PASSWORD = "zuuxlcqvdwtnvrtx"
MY_LAT = 10.823099
MY_LONG = 106.629662


# ---------------------------- IS ISS OVERHEAD ------------------------------- #
def is_issoverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

# ---------------------------- IS IT NIGHT ------------------------------- #