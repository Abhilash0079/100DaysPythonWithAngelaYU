import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": "f*454***f3r**l",
    "username": "abhilash1307",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)
