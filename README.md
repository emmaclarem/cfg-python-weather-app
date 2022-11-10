![cfgpythonheaderimage](https://user-images.githubusercontent.com/104512014/198839753-d1895769-875c-424c-bf50-bd40164fd41c.jpg)

![img](https://img.shields.io/badge/status-in%20progress-ff69b4) ![img2](https://badgen.net/pypi/python/black)

## About
This is my final project for the Code First Girls Python & Apps Kickstarter course, built in collaboration with my teammate [Nicolette Bell](https://github.com/nicolettebell).  
Team Duck! 🦆🦆🦆

## The project must:
- [x] Accept a city name as input from the user
- [x] Allow user to specify a country if there are multiple cities with the same name
- [x] Sanitize user input 
- [x] Convert user input string into latitude and longitude
- [x] Make a request to the API with the requested location's latitude and longitude as part of the search query
- [x] Get the returned values from the API response
- [x] Display the weather from the inputted location

## The project should:
- [x] Covert weather code into real weather value as a string
- [x] Be a reusable function so it can be re-run to get multiple locations without ending and restarting 
- [x] Handle user inputs that are not a real city/country or are gibberish
- [x] Handle inputs to the Y/N questions that aren't Y or N
- [x] Allow the user to specify a country if they enter a city name which is present in more than one country

## The project could:
- [ ] Have a web-based visual interface for input and to display the weather data
- [x] Allow a 'random' request to pull any city
- [x] Have ducks? 🦆

## Reflection
### 1. What was the original plan for the project?
A simple weather app that could take user input for a city, and then grab the requested location's weather data from an API and show it to the user.
### 3. What does the project actually do?
We completed the original plan, and then added several additional features. These include:
- being a reusable function so the code can be re-run to get multiple locations without ending and restarting 
- handling user inputs that are not a real city/country or are gibberish
- allowing the user to specify a country if they enter a city name which is present in more than one country
- handling inputs to the Y/N questions that aren't Y or N
- having a 'random' request that pulls a random city
- added duck emojis
### 5. Give a brief explanation of an interesting piece of code in the project.
When trying to work out how to handle user input that wasn't a real city name, we decided to add in try/except blocks (which weren't covered in the course).
```python
try:
  print(f"You've asked to see the weather in {location.address}.")
except AttributeError:
  print("I don't think that's a real place, please try again!")
  return
```
This code tries to run the intended output, but if the API returns an AttributeError it will exit the reusable part of the function and ask if you want to see another location, starting the whole flow again. 
### 7. What's one thing that you learned during the project?
Our biggest takeaway from this project was learning how to use APIs. Figuring out what data we wanted from the returned JSON files and how to access those particular bits, especially when data we wanted was in nested dictionaries, was a great learning experience. We also built in a lot of redundancies and error handling to try to keep the user in the flow of the code, whether their input was expected or unexpected. 
### 8. What was a difficult part of the project that you solved?
Adding in the option to generate a random city was unexpectedly difficult. First we had to find another API from which to get a list of city names to randomly pull from. Once we had that generating a random city, we realized that we needed to swap around loads of different code snippets to alter the control flow to get it to work as intended. Far more complex than we'd anticipated! 
### 9. What would you do if you had more time on the project?
We'd really like to connect it to a web frontend and create a full-on web-based weather app in the near future! With ducks, of course. 🦆



