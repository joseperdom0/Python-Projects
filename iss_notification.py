import requests
from datetime import datetime

# MY_LAT = 51.507351 # Your latitude
# MY_LONG = -0.127758 # Your longitude

MY_LAT = 30.507351  # test latitude
MY_LONG = 80.127758  # test longitude


def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_latitude)
    print(iss_longitude)
    # Your position is within +5 or -5 degrees of the ISS position.

    if iss_latitude + 5 > MY_LAT > iss_latitude - 5 and iss_longitude + 5 > MY_LONG > iss_longitude - 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunrise > time_now > sunset:
        return True


if is_overhead() and is_night():
    # TODO send email
    print("sending email...")
