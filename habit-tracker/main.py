import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "oDo361Itx4b5687rDgVB0je9xV",
    "username": "lenguyenquocan116",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)