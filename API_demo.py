import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# https://www.httpstatuses.org/
response.raise_for_status()

data = response.json()
iss_position = response.json()["iss_position"]

print(data)
print(iss_position)
                                                                    
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(longitude, latitude)