from pyowm.owm import OWM
from pyowm.utils import timestamps
import datetime
from WeatherCommands import OWMCommands

ch = OWMCommands

weather = ch.getWeatherDict(ch,place="New York, US")
print(weather)

ch.getWind(ch,place="New York, US")
