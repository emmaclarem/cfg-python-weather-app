## Must:
- [x] Accept a city name as input from the user
- [x] Allow user to specify a country if there are multiple cities with the same name
- [ ] Sanitize user input (the geolocator seems to do this automatically, test further to see if we need to add our own)
- [x] Convert user input string into latitude and longitude
- [x] Create a function that makes a request to the API with the requested location as part of the search query
- [x] Get the returned values from the API response
- [x] Display the weather from the inputted location

## Should:
- [x] Covert weather code into real weather value as a string
- [ ] Make the code into a function so it can be reused to get multiple locations without resetting
- [ ] Error handling in case the user inputs gibberish or anything that's not a real city/country
- [ ] Handle inputs to the Y/N questions that aren't Y or N

## Could:
- [ ] Create a visual interface for input and to display the weather data
- [ ] Ducks? 🦆
- [ ] Allow a 'random' request to pull any city





