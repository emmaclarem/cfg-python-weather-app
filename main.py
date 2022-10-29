import geopy
from geopy.geocoders import Nominatim
import requests


  # Get user input, then turn input from city name into latitude & longitude to be used in API call
address = (input("Which city do you want to get the weather for? "))
geolocator = Nominatim(user_agent="N")
location = geolocator.geocode(address)
  
# Check if city pulled is the correct one and if not, add country to lat/long request
correct = input("Is this correct? Y/N \n").upper().strip()
while correct != "Y" and correct != "N":
  correct = input("Please input either Y or N to continue. \n").upper().strip()
if correct == "Y":
  pass
elif correct == "N":
  country = input("What country is your city in? ")
  location = geolocator.geocode(address + "," + country)

#print(location.address)
#print((location.latitude, location.longitude))

# API call using the latitude and logitute parameters derived from the user input
url = f"https://api.open-meteo.com/v1/forecast?latitude={location.latitude}&longitude={location.longitude}&current_weather=true&windspeed_unit=mph"
response = requests.get(url)
#print(response)
weather = response.json()
#print(weather['current_weather'])

weathercode = weather["current_weather"]["weathercode"]
if weathercode == 0:
  weathercondition = "clear skies"
elif weathercode == 1:
  weathercondition = "mostly clear"
elif weathercode == 2:
  weathercondition = "partly cloudy"
elif weathercode == 3:
  weathercondition = "overcast"
elif weathercode == 45 or weathercode == 48:
  weathercondition = "foggy"
elif weathercode == 51 or weathercode == 53 or weathercode == 55:
  weathercondition = "drizzling"
elif weathercode == 56 or weathercode == 57:
  weathercondition = "light hail"
elif weathercode == 61:
  weathercondition = "light rain"
elif weathercode == 63:
  weathercondition = "moderate rain"
elif weathercode == 65:
  weathercondition = "heavy rain"
elif weathercode == 66 or weathercode == 67:
  weathercondition = "hailing"
elif weathercode == 71:
  weathercondition = "light snow"
elif weathercode == 73:
  weathercondition = "moderate snow"
elif weathercode == 75 or weathercode == 77:
  weathercondition = "heavy snow"
elif weathercode == 80 or weathercode == 81 or weathercode == 82:
  weathercondition = "rain showers"
elif weathercode == 85 or weathercode == 86:
  weathercondition = "snow showers"
elif weathercode == 95:
  weathercondition = "thunderstorms"
elif weathercode == 96 or weathercode == 99:
  weathercondition = "thunderstorms with hail"
else:
  weathercondition = "none"

print("The current temperature there is: " + str(weather["current_weather"]["temperature"]) + u"\u2103" + " .")
print("The current weather there is: " + str(weathercondition))



