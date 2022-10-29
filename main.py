import geopy
from geopy.geocoders import Nominatim
import requests


  # Get user input, then turn input from city name into latitude & longitude to be used in API call
address = (input("Which city do you want to get the weather for? "))
geolocator = Nominatim(user_agent="N")
location = geolocator.geocode(address)
  
print(f"You've asked to see the weather in {location}.")
#print(location.address)
#print((location.latitude, location.longitude))

# API call using the latitude and logitute parameters derived from the user input
url = f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&current_weather=true&windspeed_unit=mph"
response = requests.get(url)
#print(response)
weather = response.json()
#print(weather['current_weather'])

print("The current weather there is: " + str(weather["current_weather"]))



