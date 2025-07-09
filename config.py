import os

class Config(object):
    BOT_TOKEN = os.environ.get("")
    API_ID = int(os.environ.get("27775431"))
    API_HASH = os.environ.get("b70bb1d45a1d05236671d4cc615e40f9")
    AUTH_USER = os.environ.get('AUTH_USERS', '6414266397').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " 🆂🆄🅹🅰🅻"
