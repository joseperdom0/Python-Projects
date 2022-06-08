import requests

API_KEY = "fc5fc9e9867b9707e3adc54517440b8d"
LAT = "43.653225"
LONG = "-79.383186"
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
}

api_response = requests.get(ENDPOINT, params= weather_params)

print(api_response.status_code)
print(api_response.json())