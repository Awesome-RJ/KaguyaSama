import json
import os

def get_user_list(config, key):
    with open('{}/tg_bot/{}'.format(os.getcwd(), config), 'r') as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1403468217:AAEQWjrQg2E61WOakVJk4E82Nq0LvwSCBZw"
    OWNER_ID = "1432652637"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "UdaySriHarshaD"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://fateunion:fateunion2@database-1.c5fnisvncgjx.us-east-2.rds.amazonaws.com:5432/dbname'  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    GBAN_LOGS = -1001175530481 #Channel ID here with -
    LOAD = []
    NO_LOAD = ['translation', 'rss']   
    WEBHOOK = False
    URL = None
    API_ID = 1395919
    API_HASH = 'bbf3cae5ef0d6a1fb42b4cf6aed80f50'

    # OPTIONAL
    #ID Seperation format [1,2,3,4]
    SUDO_USERS = get_user_list('elevated_users.json', 'sudos')  # List of id's -  (not usernames) for users which have sudo access to the bot.
    DEV_USERS = get_user_list('elevated_users.json', 'devs')  # List of id's - (not usernames) for developers who will have the same perms as the owner
    SUPPORT_USERS = get_user_list('elevated_users.json', 'supports')  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = get_user_list('elevated_users.json', 'whitelists')  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = False
    STRICT_GMUTE = False
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as /
    CASH_API_KEY = None # Get one from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = None # Get one from https://timezonedb.com/register
    API_OPENWEATHER = False #Get API_OPENWEATHER FROM OFFICAL SITE https://da.gd/VAW3
    AI_API_KEY = None # Coffeehouse chatbot api key, get one from https://coffeehouse.intellivoid.info/
    WALL_API = None # Get one from https://wall.alphacoders.com/api.php
    TIGER_USERS = get_user_list('elevated_users.json', 'tigers')
    DONATION_LINK = None
    SPAMMERS = get_user_list('elevated_users.json', 'spammers')


class Production(Config):
    LOGGER = True
class Development(Config):
    LOGGER = True
