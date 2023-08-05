import requests 
import json
from config import weatherAPIKey

#SUMMARY: HTTP request --> Response object --> JSON --> dicitonary 
# URL query parameters for openWeatherAPI URL: q=location, appid =api key 
#NOTE: when uploading to github put api keys in a .gitignore file and import into needed files
url = f"https://api.openweathermap.org/data/2.5/weather?q=San Francisco&appid={weatherAPIKey}"
#use requests library to get HTTP request (sending message from browser to server, asking for info) .get(url) gives us the webpage at that address in the form of a Response object 
response = requests.get(url) 
#print(help(response)) --> list in detail the methods of Response Object
#response.text --> content of the response in unicode (HTML, JSON, etc), in this case a JSON
# json.loads() takes the JSON and formats it into a dictionary 
data = json.loads(response.text) 

#dictionary.get(keyname, value) -- keyname, value (optional) = default return
temperature = data.get('main', {}).get('temp')
wind = data.get('wind').get('speed') * 2.2369
temperature_f = temperature * 9/5 - 459.67 
# convert from Kelvin to Fahrenheit
print(f'The current temperature in San Francisco is {temperature_f:.1f}°F.') 
print(f'The current wind speed in San Francisco is {wind:.1f} mph') 
# the f'{variable}' is a string literal. the .1f tells it to specify to a float that's one decimal
print(" ")


