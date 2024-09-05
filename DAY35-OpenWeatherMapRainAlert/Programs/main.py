import requests

MY_LAT = 25.475201  # Your latitude
MY_LONG = 85.708000  # Your longitude
API_KEY = "cd9845ae76d464d0c03df175b87d0b44"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

data = response.json()
print(data)
