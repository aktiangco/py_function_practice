# Activity: Analyze the Best Golf Day
#! cd into: day4
#! cd into: day4_packages
# *! To check: python3 scripts.py
# Requesting API Data
import pprint
import requests
import json
from matplotlib import pyplot as plt # importing the module that supports drawing a graph
from datetime import datetime # importing the module that allows us to access the current time
from dotenv import load_dotenv
import os # to access environment variables using "os.environ"

load_dotenv() # Load environment variables from .env file

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.environ.get("API_KEY") # to get it from ".env"
CITY = os.environ.get("CITY")
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

try:
    # Send request to the OpenWeatherMap API
    response = requests.get(URL)
    response.raise_for_status()  # Check for any request errors
    data = response.json()  # Parse the response JSON data

    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)  # Print the formatted JSON data

    forecast_list = data['forecast']

    today = datetime.now().strftime("%b-%d-%Y")

    to_graph = {}
    count = 1
    for day in forecast_list:
        current_date = int(today[4:6]) + count
        this_day = f"{today[0:4]}{current_date}{today[6:]}"
        count += 1 if current_date <= 31 else 1

        day['wind'] = 0 if day['wind'][0] == ' ' else int(day['wind'][:2])

        to_graph[this_day] = day['wind']

    # Plotting the graph
    plt.xlabel('Date')
    plt.ylabel('Wind Speed km/h')
    plt.scatter(to_graph.keys(), to_graph.values())
    plt.show()

except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON response: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
