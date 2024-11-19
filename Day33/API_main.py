import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# print(response)
print(response.status_code)

# In Python, raise Exception is used to explicitly raise an exception, 
# which interrupts the normal flow of a program and triggers the error-handling mechanism.
# if response.status_code == 404:
#     raise Exception("That resource does not exist.") # raise a specifc exception
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.")

# but instead of doing it manually
# we can use the request module
response.raise_for_status()

# to get acutal data
data = response.json()

# we can use it like python dictionary
# iss_postion = data["iss_postion"]
# longitude = data["iss_position"]["longitude"]
print(data)