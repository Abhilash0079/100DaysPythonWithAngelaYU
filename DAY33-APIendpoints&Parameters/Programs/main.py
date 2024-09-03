import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response)

# Raise the exception
response.raise_for_status()

# JSON Data
data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
