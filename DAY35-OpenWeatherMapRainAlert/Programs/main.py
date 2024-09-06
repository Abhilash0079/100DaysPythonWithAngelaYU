import requests
from twilio.rest import Client

MY_LAT = 28.613939  # Your latitude
MY_LONG = 77.209023  # Your longitude
API_KEY = "*******07*******d7be******7ba*****"
account_sid = "A****2e2ad7*********e45**********3"
auth_token = "*****dff*******d12*******cd****"

# twilio_code = "4X6V54S6U5URFA39Z8PDLWET"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring your ☔",
        from_='+14433907301',
        to='+917004605633'
    )

    print(message.status)
