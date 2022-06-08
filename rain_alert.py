import requests

API_KEY = "fc5fc9e9867b9707e3adc54517440b8d"
LAT = "43.653225"
LONG = "-79.383186"
url_api = "https://api.openweathermap.org/data/2.5/weather?lat="+LAT+"&lon="+LONG+"&appid="

api_response = requests.get(url= url_api+API_KEY)

print(api_response)
print(api_response.json())