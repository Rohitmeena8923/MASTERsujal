import os

class Config(object):
    BOT_TOKEN = os.environ.get("")
    API_ID = int(os.environ.get("15964777"))
    API_HASH = os.environ.get("ef448f85b780cdf26f8ffe390a5d8262")
    AUTH_USER = os.environ.get('AUTH_USERS', '944358553').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " 🆂🆄🅹🅰🅻"
