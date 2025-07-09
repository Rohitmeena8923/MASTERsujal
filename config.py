import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")                       # env var name = BOT_TOKEN, default empty string
    API_ID = int(os.environ.get("API_ID", "27775431"))                 # env var name = API_ID, default "27775431"
    API_HASH = os.environ.get("API_HASH", "b70bb1d45a1d05236671d4cc615e40f9")  # env var name = API_HASH, default given
    AUTH_USER = os.environ.get('AUTH_USERS', '6414266397').split(',')  # same, with default
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " 🆂🆄🅹🅰🅻"