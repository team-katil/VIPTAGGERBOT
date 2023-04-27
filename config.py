import os
import heroku3
from telethon import TelegramClient, events ,
#
# Here Don't Worry 
# 
# 
api_id = "11660229"
api_hash = "b89dc605daa9a5e957559402cc19856b"
bot_token = "6076917136:AAHY2H09i7E-0MRPteUeh9HdJ_0V8Qq3yIs"

# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
USERNAME = "viptaggerbot"
log_group = "-1001827910417"
startmessage = "\n\n• IN YOUR GROUP ALMOST ALL MEMBER I CAN TAG . . . • CLICK ALL COMMANDS BUTTON AND CHECK . . ."
commands = "♨️ all commands ;\n\n» /utag   <  𝗆𝖾𝗌sage  >\n   - Members of 5 tags .\n\n» /tag   <  𝗆𝖾𝗌sage  >\n   - tag one by one members .\n\n» /atag   <  𝗆𝖾𝗌sage  >\n   - tag only admins .\n\n» /etag   <  𝗆essage  >\n   - tag with emoji .\n\n» /stag   <  𝗆𝖾𝗌sage  >\n   - tag member with special word .\n\n» /cancel =>\n   - cancel tagging process ."
groupstart = "• Active now I am working . . .\n\n• commands To see For your bot Inside start it login . . ."
support = "katilsupport"
owner = "katil_your_dad"
