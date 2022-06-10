import requests
import os

API_KEY = os.environ.get("API_KEY")
LAT = "43.653225"
LONG = "-79.383186"
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

api_response = requests.get(ENDPOINT, params= weather_params)

print(api_response.status_code)
print(api_response.json())

for hour in range(12):
    print(api_response.json()['hourly'][hour]['weather'][0]['id'])
    if api_response.json()['hourly'][hour]['weather'][0]['id'] < 700:
        print('Bring an umbrella')

#TODO import twilio.rest etc
# https://www.twilio.com/
