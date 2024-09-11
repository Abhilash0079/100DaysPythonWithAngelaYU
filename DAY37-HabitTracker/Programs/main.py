import requests

TOKEN = "f*454***f3r**l"
USERNAME = "abhilash1307"
GRAPH_ID = "graph1"

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
    "id": GRAPH_ID,
    "name": "Coding Practice",
    "unit": "commit",
    "type": "int",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response2 = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response2.text)

# 3. Get the graph
# https://pixe.la/v1/users/abhilash1307/graphs/graph1.html

# 4. Post value on the graph

PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": "20240911",
    "quantity": "5",
}

response3 = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)
print(response3.text)
