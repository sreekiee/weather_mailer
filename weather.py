
import requests

def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Vienna,Austria&appid=4c689e2286ceeb7c7cc9a2a3ed1e0da6'
    weather_request = requests.get(url)
    weather_json = weather_request.json()

    description = weather_json['weather'][0]['description']
    

    temp_min = weather_json['main']['temp_min']
    

    temp_max = weather_json['main']['temp_max']
    

    forecast = 'The Circus forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min)) + '.'

    return forecast
