import requests
import os
import logging
from datetime import datetime

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=f'%(asctime)s - %(name)s - %(levelname)s - %(message)s')

key = os.environ.get('WEATHER_API_KEY')

url = 'https://api.openweathermap.org/data/2.5/forecast'

location = input('Where would you like to get the weather report from? ')
location.strip()
query = {'q': location, 'units': 'imperial', 'appid': key} #Store users location in query

try:
    data = requests.get(url, params=query).json()
    list_of_forecasts = data['list']  #Add entire weather record into list

    for forecast in list_of_forecasts:
        temp = forecast['main']['temp']
        timestamp = forecast['dt']  #dt has the dates for each recording
        date = datetime.fromtimestamp(timestamp)  #I chose to use UTC since it's a common time in all computers

        print(f'The temp was {temp}F on {date}') 
except Exception as ex:
    logging.exception
    print('Unable to process request')