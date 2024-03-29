import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

OWNER = ["m_2_r_k"]
OWNER_NAME = "مِاެࢪڪكَ ⌯ 𝙈𝙍𝙆𝙫꙱🚸"
BOT_TOKEN = getenv("BOT_TOKEN")
DATABASE = getenv("MONGO_DB_URI", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
CHANNEL = "https://t.me/ucriss"
GROUP = "https://t.me/HAR_I7"
VID_SO = "https://graph.org/file/6bc77af2b8e2efb347e11.jpg"
PHOTO = "https://graph.org/file/6bc77af2b8e2efb347e11.jpg"
LOGS = "agnabyo"
