# Final Class Project Weather Program
# CIS 245 - Michael Montana
# 4 March 2022

import json
from datetime import datetime
import requests


# API KEY
API_key = "bcdc13f8e0ce619ad2cd3d229a3bdb19"

# This stores the url
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def zipCode():
    global final_url
    final_url = (base_url) + 'zip=' + (location) + \
        '&units=imperial&appid=' + (API_key)


def cityName():
    global location
    global final_url
    final_url = (base_url) + 'q=' + (location) + \
        '&units=imperial&appid=' + (API_key)


def weather_display(weather_data):  # preparing JSON for display in python
    time = weather_data['dt']
    city = weather_data['name']
    country = weather_data['sys']['country']
    latitude = weather_data['coord']['lat']
    longitude = weather_data['coord']['lon']
    description = weather_data['weather'][0]['description']
    temp = weather_data['main']['temp']
    hightemp = weather_data['main']['temp_max']
    lowtemp = weather_data['main']['temp_min']
    wind_speed = weather_data['wind']['speed']
    press = weather_data['main']['pressure']
    humid = weather_data['main']['humidity']

    formattime = datetime.utcfromtimestamp(int(time))
    print(formattime.strftime("\nDate: %d.%m.%y\nTime: %H:%M:%S UTC"))

    print('\nCity: ' + (city))
    print('Country: ' + (country))
    print('\nLatitude: {}°'.format(latitude))
    print('Longitude: {}°'.format(longitude))
    print('\nDescription: {}'.format(description))
    print('Humidity: {}%'.format(humid))
    # to type degree symbol = Alt+0176
    print('\nCurrent Temperature: {}° fahrenheit'.format(temp))
    print('High Temperature: {}° fahrenheit'.format(hightemp))
    print('Low Temperature: {}° fahrenheit'.format(lowtemp))
    print('\nWind Speed: {} mph'.format(wind_speed))
    print('Pressure: {} hPa'.format(press))


def main():
    global location
    global final_url
    yeslist = ['y', 'ye', 'yes', '']
    searchAgain = 'yes'
    while searchAgain in yeslist:
        # welcome message
        print(str('Current Weather Search').center(
            100, '_') + ('\n'))

        # This will ask the user to enter city ID
        location = input("Enter a city's name or zip code:\n")
        try:
            int(location) == int(location)  # verify numbers for zip code
            zipCode()
        except:  # if not numbers for zip city name
            cityName()

        connectStat = requests.get(final_url)
        try:
            connectStat.raise_for_status()
            print('\nConnection established!')
        except:
            print('\nUnable to establish a connection!\n')
            continue
        weather_data = json.loads(connectStat.text)
        weather_display(weather_data)

        searchAgain = input(
            '\nWould you like to see the weather in another location (yes/no)?\n').lower()
        if (searchAgain) not in yeslist:
            print('\nThank you for using my weather program, Good-Bye!')
            exit


if __name__ == "__main__":
    main()
