import os

class Config(object):
    BOT_TOKEN = os.environ.get("8157250784:AAEA7CZdV2HkAmRFFG_8cLt9eY9eUT3I2Pk")
    API_ID = int(os.environ.get("26330942"))
    API_HASH = os.environ.get("5de9fd033aa828dfd3bf0c28adeee660")
    AUTH_USER = os.environ.get('AUTH_USERS', '6883471516').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = "🆂🆄🅹🅰🅻"
