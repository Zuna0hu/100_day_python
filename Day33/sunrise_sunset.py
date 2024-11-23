import requests

MY_LAT = 45.501690
MY_LONG = -73.567253

my_params = {
    "lat": MY_LAT, # need quotes
    "lng": MY_LONG,
    "formatted": 1
}
# get from API
response = requests.get(url="https://api.sunrise-sunset.org/json", params=my_params)
# or
# my_url = f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}"
# response = requests.get(url=my_url)

# need params
response.raise_for_status()

data = response.json()

# get sunrise and sunset
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise)
print(sunset)