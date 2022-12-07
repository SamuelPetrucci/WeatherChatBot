from pyowm import OWM
import datetime
from WeatherCommands import OWMCommands
from groupy.client import Client
from Token import bot_id,groupyToken,groupy_id,WeatherKey

client = Client.from_token(groupyToken)
group = client.groups.get(groupy_id)
place = "New York, US"

class CommandPractice:
    """
    This class consist of trial functions for my Groupme Bot
    """
    def __init__(self):
        self.owm = OWM(WeatherKey)
        self.mgr = self.owm.weather_manager()
        self.weather = OWMCommands
        self.place = "New York, US"

        ##self.place = self.getLocation
        self.commandList = {'!help': self.help,
                            "!commands": self.command,
                            "!setLocation": self.setLocation,
                            "!getTemperature": self.getTemp,
                            "!getWind": self.getWind,
                            "!getVisibility": self.getVisibility,
                            "!getSunRise/Set": self.getSunRiseSet,
                            "!getPressure": self.getPressure
                            }
    def help(self):
        print("This code ran.")
        client.bots.post(bot_id=bot_id, text="Here's how I can help?")

    def command(self):
        message = ""
        for command in self.commandList:
            message += command + "\n"
        client.bots.post(bot_id=bot_id, text=message)


    def getTemp(self):
        tempNYC = self.weather.getCurrentTemp(self,place=self.place)
        message = str(tempNYC)
        client.bots.post(bot_id=bot_id, text=message)

    def getWind(self):
        observation = self.mgr.weather_at_place(self.place)
        weather = observation.weather
        wind_dict = weather.wind()
        wind_speed = str(wind_dict['speed'])
        wind_deg = wind_dict['deg']
        wind_dir = ''
        if wind_deg >= 0 and wind_deg <= 29:
            wind_dir += "N"
        elif wind_deg >=30 and wind_deg <= 70:
            wind_dir += "NE"
        elif wind_deg >= 71 and wind_deg <= 110:
            wind_dir += "E"
        elif wind_deg >= 111 and wind_deg <= 155:
            wind_dir += "SE"
        elif wind_deg >= 156 and wind_deg <= 199:
            wind_dir += "S"
        elif wind_deg >= 200 and wind_deg <= 250:
            wind_dir += "SW"
        elif wind_deg >= 256 and wind_deg <= 289:
            wind_dir += "W"
        elif wind_deg >= 290 and wind_deg <= 340:
            wind_dir += "NW"
        elif wind_deg >= 341 and wind_deg <= 359:
            wind_dir += "N"

        message = f"{place} \nWind Speed: " + wind_speed + " mph\n " \
                                "Wind Dircteion: " + wind_dir
        client.bots.post(bot_id=bot_id, text=message)

    def getVisibility(self):
        obs = self.mgr.weather_at_place(self.place)
        visibility_in_miles = obs.weather.visibility(unit='miles')
        message = f'Currently the Visibility in {self.place}: {visibility_in_miles}mi'
        client.bots.post(bot_id=bot_id, text=message)


    def getPressure(self):
            pressure_dict = self.mgr.weather_at_place(place).weather.barometric_pressure()
            pressure = pressure_dict['press']
            message = f'Barometric Pressure in {place}: {pressure} hPa '
            client.bots.post(bot_id=bot_id, text=message)

    def getSunRiseSet(self):
        observation = self.mgr.weather_at_place(place)
        weather = observation.weather
        sunrise_unix = weather.sunrise_time()  # default unit: 'unix'
        sunrset_unix = weather.sunset_time()  # default unit: 'unix'
        sunrise_time = datetime.datetime.fromtimestamp(sunrise_unix).time()
        sunset_time = datetime.datetime.fromtimestamp(sunrset_unix).time()
        message = f'Today in {place}, the sun will rise at {sunrise_time} a.m.'\
                  f'\n and the sun will set at {sunset_time}p.m.'
        client.bots.post(bot_id=bot_id, text=message)

    def handleMessage(self,message):
        message = message.split()
        if len(message) == 1:

            command = message[0]
            print("This code ran 2")
            if command in self.commandList:
                print("inside if: " + command)
                self.commandList[command]()
        elif len(message) == 2:
            command = message[0]
            parameter = message[1]
            if command in self.commandList:
                print("inside if: " + command)
                self.commandList[command](parameter)

    def setLocation(self,location):
        self.place = location
        if "-" in location:
            location = location.replace('-', ' ')
        bot_response = "The new location is " + str(location)
        client.bots.post(bot_id=bot_id, text=bot_response)



