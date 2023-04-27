import os
import heroku3
from telethon import TelegramClient, events
#
# Here Don't Worry 
# 
# 
api_id = int(os.environ.get("APP_ID", "11660229"))
api_hash = os.environ.get("API_HASH", "b89dc605daa9a5e957559402cc19856b")
bot_token = os.environ.get("TOKEN", "6076917136:AAHY2H09i7E-0MRPteUeh9HdJ_0V8Qq3yIs")

# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
USERNAME = os.environ.get("USERNAME", "KATIL_YOUR_DAD")
log_group = int(os.environ.get("LOG_GROUP", "-1001827910417"))
startmessage = os.environ.get("startmessage")
commands = os.environ.get("commands")
groupstart = os.environ.get("groupstart")
support = os.environ.get("support")
owner = os.environ.get("owner")
