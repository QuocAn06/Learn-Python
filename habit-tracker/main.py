import requests
from datetime import datetime

USERNAME = "lenguyenquocan116"
TOKEN = "oDo361Itx4b5687rDgVB0je9xV"
GRAPH_ID = "graph01"

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
    "id": GRAPH_ID,
    "name": "Learning English Graph",
    "unit": "Minute(s)",
    "type": "int",
    "color": "sora",
    "timezone": "Asia/Ho_Chi_Minh",
}

graph_headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=graph_headers)
# print(response.text)

## Post value to the graph
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


today = datetime.today().strftime('%Y%m%d')
print(today)

pixel_data = {
    "date": today,
    "quantity": "60"
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_data, headers=graph_headers)
# print(response.text)

## Update value to the graph
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

new_pixel_data = {
    "quantsity": "45"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=graph_headers)
# print(response.text)

## Delete value of the graph
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"

# response = requests.delete(url=delete_endpoint, headers=graph_headers)
# print(response.text)
