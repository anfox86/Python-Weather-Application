#File: AssignmentFinal_Fox.py
#Name: Andrea Fox
#Final Assignment - Weather Application

import requests #to access the requests library
import json #to view the weather data via json
#allows me to look up weather by city and display weather output
def retrieveWeatherByCity(city):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    querystring = {"q": city, "appid": "272918e7444b68caccb31c4aae945a4c", "units": "imperial"}
    headers = {'cache-control': 'no-cache'}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
    except requests.exceptions.RequestException as e:
        print('You have received an error, please try again.')
    weather_dict = json.loads(response.text)
    weather = weather_dict.get('weather')
    print("The weather in ", city, " is ", weather[0].get('description'))
    temp_max = weather_dict.get('main').get('temp_max')
    print("High temp:" + str(temp_max))
    temp_min = weather_dict.get('main').get('temp_min')
    print("Low temp:" + str(temp_min))
    temp = weather_dict.get('main').get('temp')
    print("Current temp:" + str(temp))
    humidity = weather_dict.get('main').get('humidity')
    print("Humidity is:" + str(humidity))
#allows me to look up weather by zipcode and display weather output
def  retrieveWeatherByZip(zipcode):
    url = 'https://api.openweathermap.org/data/2.5/weather'
    querystring = {"q": zipcode, "appid": "272918e7444b68caccb31c4aae945a4c", "units": "imperial"}
    headers = {'cache-control': 'no-cache'}
    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
    except requests.exceptions.RequestException as e:
        print('You have received an error, please try again.')
    weather_dict = json.loads(response.text)
    weather = weather_dict.get('weather')
    print("The weather in ", zipcode, " is ", weather[0].get('description'))
    temp_max = weather_dict.get('main').get('temp_max')
    print("High temp:" + str(temp_max))
    temp_min = weather_dict.get('main').get('temp_min')
    print("Low temp:" + str(temp_min))
    temp = weather_dict.get('main').get('temp')
    print("Current temp:" + str(temp))
    humidity = weather_dict.get('main').get('humidity')
    print("Humidity is:" + str(humidity))
#Allows user to make selection on whether they would like to view weather by city or zip
def main():
    print('Welcome to the Daily Weather Report')
    ask_user = int(input('Would you like to lookup weather data by US City or zip code? Enter 1 for US City or 2 for zip. \n'))
    while ask_user != 0:
        if ask_user == 1:
            city = input('What city?')
            retrieveWeatherByCity(city)
            ask_user = int(input('Would you like to see another location? Enter 1 for US City, 2 for zipcode, or 0 to exit'))
        elif ask_user == 2:
            zipcode = input('What zipcode?')
            retrieveWeatherByZip(zipcode)
            ask_user = int(input('Would you like to see another location? Enter 1 for US City, 2 for zipcode, or 0 to exit.'))
        else:
            ask_user = int(input('I did not understand you.  Please enter  1 or 2: \n'))
if __name__ == '__main__':
    main()


