import requests
from datetime import datetime

MY_LAT = 45.501690
MY_LONG = -73.567253

my_params = {
    "lat": MY_LAT, # need quotes
    "lng": MY_LONG,
    "formatted": 0
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

# get the hour and minute
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunrise_min = sunrise.split("T")[1].split(":")[1]
sunset_hour = sunset.split("T")[1].split(":")[0]
sunset_min = sunset.split("T")[1].split(":")[1]

# print(sunrise)
# print(sunset)

# UTC (Coordinated Universal Time) by default, not local time. 
# print(f"sunrise time in Montreal(UTC): {sunrise_hour}h{sunrise_min}")
# print(f"sunset time in Montreal(UTC): {sunset_hour}h{sunset_min}")

# Get the current date
now = datetime.now()

# approximately determine if it's DST in Montreal
if (now.month > 3 and now.month < 11) or (now.month == 3 and now.day >= 8) or (now.month == 11 and now.day < 7): # not accurate
    # minus 4
    print(f"sunrise time in Montreal(local): {(int(sunrise_hour)+20)%24}h{sunrise_min}")
    print(f"sunset time in Montreal(local): {(int(sunset_hour)+20)%24}h{sunset_min}")
else:
    # minus 5
    print(f"sunrise time in Montreal(local): {(int(sunrise_hour)+19)%24}h{sunrise_min}")
    print(f"sunset time in Montreal(local): {(int(sunset_hour)+19)%24}h{sunset_min}")