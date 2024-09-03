import requests
import datetime as dt

parameters = {
    "lat": 25.475201,
    "lng": 85.708000,
    "formatted": 0
}


response = requests.get("https://api.sunrise-sunset.org/json?lat=51.507351&lng=-0.127758&formatted=0")
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()


data = response.json()
# print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

# print(f"Sunrise : {sunrise} and Sunset : {sunset}")
print(f"Sunrise : {sunrise} and Sunset : {sunset}")

time_now = dt.datetime.now()
print(time_now.hour)
