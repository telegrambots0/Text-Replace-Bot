import os

class Config(object):
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6796993711:AAE_xk1idxA_FbU5mcXK5_YaZdCkI6p9PaE")

    APP_ID = int(os.environ.get("APP_ID", "27815405"))

    API_HASH = os.environ.get("API_HASH", "4e70821cd2af3322f7cf2f2887e32821")    
    
    CAPTION_TEXT = os.environ.get("CAPTION_TEXT", "Swarg Ronny")

    CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "bottom")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "27815405").split())
