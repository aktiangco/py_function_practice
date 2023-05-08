# Activity: Analyze the Best Golf Day
#! cd into: day4_packages
# *! To check: python3 scripts.py
# Requesting API Data

import pprint
import requests, json
from matplotlib import pyplot as plt # importing the module that supports drawing a graph
from datetime import datetime # importing the module that allows us to access the current time

# here we are formatting the PrettyPrinter. Try using different indents!
pp = pprint.PrettyPrinter(indent=4)
'''
# fetching API
API_URL = 'https://weather-api-node-wisc.herokuapp.com/weather/' #! API isn't working
city = 'seattle' # feel free to enter your own city here!
r = requests.get(API_URL + city)
response = r.json()
# print(response) #data is hard to read / syntax in line#11 /call on line#8
'''
from dotenv import load_dotenv 
load_dotenv() # Load environment variables from .env file

import os # to access environment variables using "os.environ"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.environ.get("API_KEY") # to get it from ".env"
CITY = os.environ.get("CITY")
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
response = requests.get(URL)
# pp.pprint(response) # to clean up your results
try:
    response.raise_for_status() # Check for any request errors
    data = response.json() # Parse the response JSON data
    pp.pprint(data) # Print the formatted JSON data
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")
except Exception as e:
    print(f"An error occurred: {e}")