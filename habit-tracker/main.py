import requests

USERNAME = "lenguyenquocan116"
TOKEN = "oDo361Itx4b5687rDgVB0je9xV"

## Create your user account
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

## Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph01",
    "name": "Learning English Graph",
    "unit": "Minute(s)",
    "type": "int",
    "color": "sora",
    "timezone": "Asia/Ho_Chi_Minh",
}

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)
print(response.text)
