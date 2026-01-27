import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","22540373"))
API_HASH = getenv("API_HASH","41c21b4f450a79e23b0ccf7593aeaad3")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","5418725646:AAHoubyDR")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://untoldp:untoldp@untoldp.zdixt.mongodb.net/?retryWrites=true&w=majority&appName=untoldp")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

# Chat id of a group for logging bot's activities
# Users & Logging
BANNED_USERS = []
LOGGER_ID = 8417510906            # apna Telegram ID yahan dal sakte ho
LOG_GROUP_ID = -1002389305159         # apna Telegram group ID yahan dal sakte ho
# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID","6391774843"))

API_URL", 'https://BabyAPI.Pro') 
API_KEY = getenv('API_KEY', 'ADMINBABYX20F56755E70E0694DDCC844F5F1BB465')

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME","lehar")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY","HRKU-76a2723e-ff3f-4191-b17f-d5a68b882cc8")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rockStar378/Kavyaone",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", "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"
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHAT", "https://t.me/+St2iiL0MMMQ2ZWM0")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/+St2iiL0MMMQ2ZWM0")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# make your bots privacy from telegra.ph and put your url here 
PRIVACY_LINK = getenv("PRIVACY_LINK", "https://files.catbox.moe/jyeumn.jpg")


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION","BQFX8FUAk5VbVlU1TIzaPtPcMvi4hT1I9YMw5xqFzCyIiopQKxRMVACAwNBghCJDHgXszS8Z97iq4vqLs70gwqAhfx5cesSoxtxMYSAEKCegjxlWSBTfc0OD5MvMaZAi0L4uQG1k0rSx3W8vEdF6y5WwBSG30G1LYUG-wW_nN8RGJrleanOXTFbDcuWYiWqQLSUfI0bxwlAwZosMutjMNBgFNm3gbyY4j7g1-br5KhQ6klGtCgLPNTv9UfrHhn54BjU4hzcd4j9Y3z0x210ahD4PiBFZ1gexLtGe5kHZendA1fImkTL80YDxYKtiJDT2Pvrqtens1Qowvj9GVPnBT4T53jRpYAAAAAHYFwJPAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://files.catbox.moe/x5lytj.jpg",
                 "https://files.catbox.moe/psya34.jpg",
                 "https://files.catbox.moe/leaexg.jpg",
                 "https://files.catbox.moe/b0e4vk.jpg",
                 "https://files.catbox.moe/1b1wap.jpg",
                 "https://files.catbox.moe/ommjjk.jpg",
                 "https://files.catbox.moe/onurxm.jpg",
                 "https://files.catbox.moe/97v75k.jpg",
                 "https://files.catbox.moe/t833zy.jpg",
                 "https://files.catbox.moe/472piq.jpg",
                 "https://files.catbox.moe/qwjeyk.jpg",
                 "https://files.catbox.moe/t0hopv.jpg",
                 "https://files.catbox.moe/u5ux0j.jpg",
                 "https://files.catbox.moe/h1yk4w.jpg",
                 "https://files.catbox.moe/gl5rg8.jpg"]

PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/nx6uds.jpg"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/nx6uds.jpg"
STATS_IMG_URL = "https://files.catbox.moe/nx6uds.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/492a3bb2e880d19750b79.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/492a3bb2e880d19750b79.jpg"
STREAM_IMG_URL = "https://graph.org/file/ff2af8d4d10afa1baf49e.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/c95a687e777b55be1c792.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/e8730fdece86a1166f608.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/0bb6f36796d496b4254ff.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )








