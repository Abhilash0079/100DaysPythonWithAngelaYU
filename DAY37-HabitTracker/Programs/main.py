import requests

TOKEN = "f*454***f3r**l"
USERNAME = "abhilash1307"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# 1. Creating a user account on Pixela
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# 2. Create a graph

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Practice",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response2 = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response2.text)
