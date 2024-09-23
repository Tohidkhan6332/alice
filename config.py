import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 22109421
API_HASH = "13946e80ec9b081f0beecca3163940a0"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7218571103:AAGJbDwpvYuCwUS4rQhz5Nfh1BNpzqJg_94"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://tohid:tohid@cluster0.rqtprv9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1001821969607

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 6077226181

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/marvelmoviehin"
SUPPORT_GROUP = "https://t.me/marval_movie_hindi_group"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


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
STRING1 = "BQEj9uwAd1e0f-YtlSP_exJUMeAINWPkkwUtM0YtZw4b9l_ah-svWm2oYC95Kxx6V4a-5StoeyGwAZ9HF8bhp5PtgOaNyRfKlNb-sDc4dJau85ibbS_qlSZoIQ3ZM2Z9FIVhhG1enWz2RdPhUOg3yQG4dYjfyso-tlgsioP-nwnba31iM0evXCK7uW1A00kWNx2adRLNpHqcVAruuVL7ScFTG3bT5NlyydBUhU2D9-_OY-roTTVwhGDevEEJqXALzbkXJndI7GiexFcPrEvfcreu9aXcaVm2-dRy3csD836CAV6vFXHoLGfzLAAHBgpFf5Qd_LNkcxjCtg_FGd0GbQonRu7FywAAAAGuQqdfAQ"
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


START_IMG_URL = "https://telegra.ph/file/042cd0b6121a7923fd5d2.jpg"

PING_IMG_URL = "https://telegra.ph/file/042cd0b6121a7923fd5d2.jpg"

PLAYLIST_IMG_URL = "https://telegra.ph/file/042cd0b6121a7923fd5d2.jpg"
STATS_IMG_URL = "https://telegra.ph/file/042cd0b6121a7923fd5d2.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/042cd0b6121a7923fd5d2.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/042cd0b6121a7923fd5d2.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/042cd0b6121a7923fd5d2.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/042cd0b6121a7923fd5d2.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/042cd0b6121a7923fd5d2.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/042cd0b6121a7923fd5d2.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/042cd0b6121a7923fd5d2.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/042cd0b6121a7923fd5d2.jpg"


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
