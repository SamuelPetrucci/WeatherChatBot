from pyowm.utils import timestamps
from pyowm.owm import OWM
import datetime

owm = OWM("78218aca21cb3e2c0377fec72a023203")
mgr = owm.weather_manager()

class OWMCommands:
    '''
    This class will handle commands that return
    weather data to a user based on a city they chose
    '''
    def __init__(self,place):
        self.place = place

    def getCurrentTemp(self,place):
        observation = mgr.weather_at_place(place)
        weather = observation.weather
        temp = weather.get_temperature()
        print(f'The Temperature of {place} Today: {temp}')

    def getPressure(self, place):
        pressure_dict = mgr.weather_at_place(place).weather.barometric_pressure()
        pressure = pressure_dict['press']
        print(f'Barometric Pressure in {place}: {pressure} hPa ')

    def getTommorowsTemp(self,place):
        tommorows_temp = mgr.forecast_at_place(place, 'daily', limit=None)
        tomorrow = timestamps.tomorrow()  # datetime object for tomorrow
        weather = tommorows_temp.get_weather_at(tomorrow)
        temp = weather.temperature('fahrenheit')
        print(f'The Weather Tomorrow in {place}: {temp}')

    def getVisibility(self,place):
        obs = mgr.weather_at_place(place)
        visibility_in_miles = obs.weather.visibility(unit='miles')
        print(f'Today Visibility in {place}: {visibility_in_miles}mi')

    def SunRiseSet(self,place):
        observation = mgr.weather_at_place(place)
        weather = observation.weather
        sunrise_unix = weather.sunrise_time()  # default unit: 'unix'
        sunrset_unix = weather.sunset_time()  # default unit: 'unix'
        sunrise_time = datetime.datetime.fromtimestamp(sunrise_unix).time()
        sunset_time = datetime.datetime.fromtimestamp(sunrset_unix).time()
        print(f'Today in {place}, the sun will rise at {sunrise_time}'
              f'\n and the sun will set at {sunset_time}.')





