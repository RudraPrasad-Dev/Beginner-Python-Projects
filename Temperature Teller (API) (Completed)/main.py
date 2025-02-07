# The Modules 
import requests  
import json

# The keywords for API
city = input("Can you please tell me the city you want to know the weather of: ")
url = f"https://api.weatherapi.com/v1/current.json?key=20415abeebb44060b66120126251601&q={city}"

# This function of requests helps to get the data of a link given
req = requests.get(url)

# Here we are doing the final touch
weather_dic = json.loads(req.text) # Converting the string to dictionary to easily get temperature
print(f"As of {weather_dic["current"]["last_updated"]}, the temperature of {city} is {weather_dic["current"]["temp_c"]} Celcius") # Printing the output