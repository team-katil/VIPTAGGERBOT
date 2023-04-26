import os
import heroku3
from telethon import TelegramClient, events
#
# Burayı gurcalama
# 
# 
api_id = int(os.environ.get("APP_ID", "9316256"))
api_hash = os.environ.get("API_HASH", "5a8a277605c3038129c536a9e79cd761")
bot_token = os.environ.get("TOKEN", "5864136148:AAGTTxKCYQm-ykN9AbEikY05M8qPcUTNiTI")

# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
USERNAME = os.environ.get("USERNAME", "Merdoobeyims")
log_qrup = int(os.environ.get("LOG_QRUP", "-1001827910417"))
startmesaj = os.environ.get("startmesaj")
komutlar = os.environ.get("komutlar")
qrupstart = os.environ.get("qrupstart")
support = os.environ.get("support")
sahib = os.environ.get("sahib")
