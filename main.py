from Bot import Bot
from Token import bot_id
from groupy.exceptions import BadResponse


while True:
    try:
        bot = Bot("SmartBot", bot_id)

    except BadResponse:
        print("Bad Response")












