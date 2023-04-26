import os
import heroku3
from telethon import TelegramClient, events
#
# Here Don't Worry 
# 
# 
api_id = int(os.environ.get("APP_ID", "9316256"))
api_hash = os.environ.get("API_HASH", "5a8a277605c3038129c536a9e79cd761")
bot_token = os.environ.get("TOKEN", "5864136148:AAGTTxKCYQm-ykN9AbEikY05M8qPcUTNiTI")

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
