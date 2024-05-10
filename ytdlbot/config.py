#!/usr/local/bin/python3
# coding: utf-8

# ytdlbot - config.py
# 8/28/21 15:01
#



import os

from blinker import signal

# general settings
WORKERS: int = int(os.getenv("WORKERS", 100))
PYRO_WORKERS: int = int(os.getenv("PYRO_WORKERS", 100))
APP_ID: int = int(os.getenv("APP_ID",23080322 ))
APP_HASH = os.getenv("APP_HASH", "b3611c291bf82d917637d61e4a136535")
TOKEN = os.getenv("TOKEN", "6931048916:AAEiwn5cej-PVBw95cqsGskW-BEGx95o4jY")

REDIS = os.getenv("REDIS", "redis")

TG_PREMIUM_MAX_SIZE = 40000000 * 1024 * 1024
TG_NORMAL_MAX_SIZE = 2012000 * 1024 * 1024
# TG_NORMAL_MAX_SIZE = 10 * 1024 * 1024


EXPIRE = 1 * 12

ENABLE_VIP = os.getenv("VIP", True)
OWNER = os.getenv("OWNER", "aryanchy449")

# limitation settings
AUTHORIZED_USER: str = os.getenv("AUTHORIZED_USER", "aryanchy449")
# membership requires: the format could be username(without @ sign)/chat_id of channel or group.
# You need to add the bot to this group/channel as admin
REQUIRED_MEMBERSHIP: str = os.getenv("REQUIRED_MEMBERSHIP", "")

# celery related
ENABLE_CELERY = os.getenv("ENABLE_CELERY", True)
BROKER = os.getenv("BROKER", f"redis://{REDIS}:6379/1")

MYSQL_HOST = os.getenv("MYSQL_HOST", "mysql")
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASS = os.getenv("MYSQL_PASS", "root")

AUDIO_FORMAT = os.getenv("AUDIO_FORMAT")
ARCHIVE_ID = os.getenv("ARCHIVE_ID")

IPv6 = os.getenv("IPv6", False)
ENABLE_FFMPEG = os.getenv("ENABLE_FFMPEG", False)

PLAYLIST_SUPPORT = os.getenv("PLAYLIST_SUPPORT", False)
M3U8_SUPPORT = os.getenv("M3U8_SUPPORT", False)
ENABLE_ARIA2 = os.getenv("ENABLE_ARIA2", False)

RATE_LIMIT = os.getenv("RATE_LIMIT", 120)
RCLONE_PATH = os.getenv("RCLONE")
# This will set the value for the tmpfile path(download path) if it is set.
# If TMPFILE is not set, it will return None and use system’s default temporary file path.
# Please ensure that the directory exists and you have necessary permissions to write to it.
# If you don't know what this is just leave it as it is.
TMPFILE_PATH = os.getenv("TMPFILE")

# payment settings
AFD_LINK = os.getenv("AFD_LINK", "Hello")
COFFEE_LINK = os.getenv("COFFEE_LINK", "hello")
COFFEE_TOKEN = os.getenv("COFFEE_TOKEN")
AFD_TOKEN = os.getenv("AFD_TOKEN")
AFD_USER_ID = os.getenv("AFD_USER_ID")
PROVIDER_TOKEN = os.getenv("PROVIDER_TOKEN") or "1234"
FREE_DOWNLOAD = os.getenv("FREE_DOWNLOAD", 1000)
TOKEN_PRICE = os.getenv("BUY_UNIT", 1)  # one USD=20 credits
TRONGRID_KEY = os.getenv("TRONGRID_KEY", "").split(",")
# the default mnemonic is for nile testnet
TRON_MNEMONIC = os.getenv("TRON_MNEMONIC", "cram floor today legend service drill pitch leaf car govern harvest soda")
TRX_SIGNAL = signal("trx_received")

PREMIUM_USER = int(os.getenv("PREMIUM_USER", "aryanchy449"))


class FileTooBig(Exception):
    pass
