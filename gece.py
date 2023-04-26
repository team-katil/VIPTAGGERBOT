#################################
# Vip Tagger Bot #
#################################
# team-katil - @katil_your_dad
# Telegram - t.me/katilupdate
# Telegram - t.me/katil_your_dad
##################################
import heroku3
import random
import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation
from config import client, USERNAME, log_group, startmessage, groupstart, commands, owner, support

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)



anlik_calisan = []
gece_tag = []


  
# start message 
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for user in client.iter_participants(event.chat_id):
     ad = f"• HELLO [{user.first_name}](tg://user?id={usr.id}) "
     await client.send_message(log_group, f"ℹ️ **New User -** \n {ad}")
     return await event.reply(f"{ad} {startmessage}", buttons=(
                      [
                       Button.url('🎉  add me in your group  🎉', f'https://t.me/{USERNAME}?startgroup=a')],
                      [Button.inline("📚  commands  ", data="commands"),
                       Button.url('📝  support  ', f'https://t.me/{support}')]
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"{qrupstart}")

# Start Button
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for user in client.iter_participants(event.chat_id):
     ad = f"• HELLO [{user.first_name}](tg://user?id={user.id}) "
     await event.edit(f"{ad} {startmessage}", buttons=(
                      [
                       Button.url('🎉  add me in your group  🎉', f'https://t.me/{USERNAME}?startgroup=a')],
                      [Button.inline("📚  commands  ", data="commands"),
                       Button.url('📝  support  ', f'https://t.me/katilsupport')]
                    ),
                    link_preview=False)

# night bird
@client.on(events.callbackquery.CallbackQuery(data="commands"))
async def handler(event):
    await event.edit(f"{commands}", buttons=(
                      [
                      Button.url('📣  𝖲𝗎𝗉𝗉𝗈𝗋𝗍  ', f'https://t.me/katilsupport'),
                      Button.url('♨️  𝖮𝗐𝗇𝖾𝗋  ', f'https://t.me/katil_your_dad')
                      ],
                      [
                      Button.inline("<  🔙 Back  >", data="start"),
                      ]
                    ),
                    link_preview=False)

# 5 li etiketleme modulü
@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("𝖤𝗌𝗄𝗂 𝖬𝖾𝗌𝖺𝗃𝗅𝖺𝗋𝗂 𝖦𝗈𝗋𝖾𝗆𝗂𝗒𝗈𝗋𝗎𝗆 ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("• 𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝖬𝖾𝗌𝖺𝗃𝗂 𝖸𝖺𝗓𝗆𝖺𝖽𝗂𝗇 ! ")
  else:
    return await event.respond("• 𝖤𝗍𝗂𝗄𝖾𝗍 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝖾 𝖻𝖺𝗌𝗅𝖺𝗆𝖺𝗆 𝗂𝖼𝗂𝗇 𝖻𝗂𝗋 𝗌𝖾𝖻𝖾𝗉 𝗒𝖺𝗓𝗂𝗇 ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "✅ merdoobey üye etiketleme işlemini başlattı . . .",
                    buttons=(
                      [
                      Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) , "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ merdobey üye işlemini durdurdu . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  )
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{msg} \n {usrtxt}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# admin etiketleme modülü
@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("𝖤𝗌𝗄𝗂 𝖬𝖾𝗌𝖺𝗃𝗅𝖺𝗋𝗂 𝖦𝗈𝗋𝖾𝗆𝗂𝗒𝗈𝗋𝗎𝗆 ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("• 𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝖬𝖾𝗌𝖺𝗃𝗂 𝖸𝖺𝗓𝗆𝖺𝖽𝗂𝗇 ! ")
  else:
    return await event.respond("• 𝖤𝗍𝗂𝗄𝖾𝗍 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝖾 𝖻𝖺𝗌𝗅𝖺𝗆𝖺𝗆 𝗂𝖼𝗂𝗇 𝖻𝗂𝗋 𝗌𝖾𝖻𝖾𝗉 𝗒𝖺𝗓𝗂𝗇 ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "✅ merdoobey 𝖠𝖽𝗆𝗂𝗇 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝗅𝖺ttı . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"• [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ merdoobey 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖽𝗎𝗋𝖽𝗎𝗋du . . .",
                    buttons=(
                      [
                       Button.url('📝  𝖪𝖺𝗇𝖺𝗅  📝', f'https://t.me/ChatKaos')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} \n {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# tek tek etiketleme modülü
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def tektag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("𝖤𝗌𝗄𝗂 𝖬𝖾𝗌𝖺𝗃𝗅𝖺𝗋𝗂 𝖦𝗈𝗋𝖾𝗆𝗂𝗒𝗈𝗋𝗎𝗆 ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("• 𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝖬𝖾𝗌𝖺𝗃𝗂 𝖸𝖺𝗓𝗆𝖺𝖽𝗂𝗇 ! ")
  else:
    return await event.respond("• 𝖤𝗍𝗂𝗄𝖾𝗍 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝖾 𝖻𝖺𝗌𝗅𝖺𝗆𝖺𝗆 𝗂𝖼𝗂𝗇 𝖻𝗂𝗋 𝗌𝖾𝖻𝖾𝗉 𝗒𝖺𝗓𝗂𝗇 ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "✅ merdobey 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝗅𝖺ttı . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"• [{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ merdobey 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖽𝗎𝗋𝖽𝗎𝗋du . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} \n {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# Emoji ile etiketleme modülü

anlik_calisan = []

tekli_calisan = []




emoji = " ❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 🙂 🙃 😉 😌 😍 🥰 😘 😗 😙 😚 😋 😛 😝 😜 🤪 🤨 🧐 🤓 😎 🤩 🥳 😏 😒 " \
        "😞 😔 😟 😕 🙁 😣 😖 😫 😩 🥺 😢 😭 😤 😠 😡  🤯 😳 🥵 🥶 😱 😨 😰 😥 😓 🤗 🤔 🤭 🤫 🤥 😶 😐 😑 😬 🙄 " \
        "😯 😦 😧 😮 😲 🥱 😴 🤤 😪 😵 🤐 🥴 🤢 🤮 🤧 😷 🤒 🤕 🤑 🤠 😈 👿 👹 👺 🤡  👻 💀 👽 👾 🤖 🎃 😺 😸 😹 " \
        "😻 😼 😽 🙀 😿 😾 ❄️ 🌺 🌨 🌩 ⛈ 🌧 ☁️ ☀️ 🌈 🌪 ✨ 🌟 ☃️ 🪐 🌏 🌙 🌔 🌚 🌝 🕊 🦩 🦦 🌱 🌿 ☘ 🍂 🌹 🥀 🌾 " \
        "🌦 🍃 🎋🦓 🐅 🐈‍⬛ 🐄 🦄 🐇 🐁 🐷 🐶 🙈 🙊 🐻 🐼 🦊 🐮 🐍 🐊 🦨 🦔 🐒 🦣 🦘 🦥 🦦 🦇 🦍 🐥 🐦 🦜 🕊️ 🦤 🦢 " \
        "🦩 🦚 🦃 🐣 🐓 🐬 🦈 🐠 🐳 🦗 🪳 🐝 🐞 🦋 🐟 🕷️ 🦑".split(" ")

@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def etag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("𝖤𝗌𝗄𝗂 𝖬𝖾𝗌𝖺𝗃𝗅𝖺𝗋𝗂 𝖦𝗈𝗋𝖾𝗆𝗂𝗒𝗈𝗋𝗎𝗆 ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("• 𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝖬𝖾𝗌𝖺𝗃𝗂 𝖸𝖺𝗓𝗆𝖺𝖽𝗂𝗇 ! ")
  else:
    return await event.respond("• 𝖤𝗍𝗂𝗄𝖾𝗍 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝖾 𝖻𝖺𝗌𝗅𝖺𝗆𝖺𝗆 𝗂𝖼𝗂𝗇 𝖻𝗂𝗋 𝗌𝖾𝖻𝖾𝗉 𝗒𝖺𝗓𝗂𝗇 ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "✅ merdobey 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝗅𝖺ttı . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) , "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ merdobey 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖽𝗎𝗋𝖽𝗎𝗋du . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  )
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt} \n {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# söz ile etiketleme modülü

soz = (
'ᴜsʟᴜᴘ ᴋᴀʀᴀᴋᴛᴇʀɪᴅɪʀ ʙɪʀ ɪɴsᴀɴɪɴ', 
'ɪʏɪʏɪᴍ ᴅᴇsᴇᴍ ɪɴᴀɴᴀᴄᴀᴋ , ᴏ ᴋᴀᴅᴀʀ ʜᴀʙᴇʀsɪᴢ ʙᴇɴᴅᴇɴ', 
'ᴍᴇsᴀғᴇʟᴇʀ ᴜᴍʀᴜᴍᴅᴀ ᴅᴇɢɪʟ , ɪᴄɪᴍᴅᴇ ᴇɴ ɢᴜᴢᴇʟ ʏᴇʀᴅᴇsɪɴ',
'ʙɪʀ ᴍᴜᴄɪᴢᴇʏᴇ ɪʜᴛɪʏᴀᴄɪᴍ ᴠᴀʀᴅɪ , ʜᴀʏᴀᴛ sᴇɴɪ ᴋᴀʀsɪᴍᴀ ᴄɪᴋᴀʀᴅɪ', 
'ᴏʏʟᴇ ɢᴜᴢᴇʟ ʙᴀᴋᴛɪɴ ᴋɪ , ᴋᴀʟʙɪɴ ᴅᴇ ɢᴜʟᴜsᴜɴ ᴋᴀᴅᴀʀ ɢᴜᴢᴇʟ sᴀɴᴍɪsᴛɪᴍ', 
'ʜᴀʏᴀᴛ ɴᴇ ɢɪᴅᴇɴɪ ɢᴇʀɪ ɢᴇᴛɪʀɪʀ , ɴᴇ ᴅᴇ ᴋᴀʏʙᴇᴛᴛɪɢɪɴ ᴢᴀᴍᴀɴɪ ɢᴇʀɪ ɢᴇᴛɪʀɪʀ', 
'sᴇᴠᴍᴇᴋ ɪᴄɪɴ sᴇʙᴇᴘ ᴀʀᴀᴍᴀᴅɪᴍ , ʙɪʀ ᴛᴇᴋ sᴇsɪ ʏᴇᴛᴛɪ ᴋᴀʟʙɪᴍᴇ', 
'ᴍᴜᴛʟᴜʏᴜɴ ᴀᴍᴀ sᴀᴅᴇᴄᴇ sᴇɴɪɴʟᴇ', 
'ʙᴇɴ ʜᴇᴘ sᴇᴠɪʟᴍᴇᴋ ɪsᴛᴇᴅɪɢɪᴍ ɢɪʙɪ sᴇᴠɪɴᴅɪᴍ', 
'ʙɪʀɪ ᴠᴀʀ ɴᴇ ᴏᴢʟᴇᴍᴇᴋᴛᴇɴ ʏᴏʀᴜʟᴅᴜᴍ ɴᴇ sᴇᴠᴍᴇᴋᴛᴇɴ', 
'ᴄᴏᴋ ᴢᴏʀ ʙᴇ sᴇɴɪ sᴇᴠᴍᴇʏᴇɴ ʙɪʀɪɴᴇ ᴀsɪᴋ ᴏʟᴍᴀᴋ', 
'ᴄᴏᴋ ᴏɴᴇᴍsɪᴢʟɪᴋ ɪsᴇ ʏᴀʀᴀᴍᴀᴅɪ ᴀʀᴛɪᴋ ʙᴏs ᴠᴇʀɪʏᴏʀᴜᴢ', 
'ʜᴇʀᴋᴇsɪɴ ʙɪʀ ɢᴇᴄᴍɪsɪ ᴠᴀʀ , ʙɪʀ ᴅᴇ ᴠᴀᴢɢᴇᴄᴍɪsɪ', 
'ᴀsɪᴋ ᴏʟᴍᴀᴋ ɢᴜᴢᴇʟ ʙɪʀ sᴇʏ ᴀᴍᴀ sᴀᴅᴇᴄᴇ sᴀɴᴀ', 
'ᴀɴʟᴀʏᴀɴ ʏᴏᴋᴛᴜ , sᴜsᴍᴀʏɪ ᴛᴇʀᴄɪʜ ᴇᴛᴛɪᴍ', 
'sᴇɴ ᴄᴏᴋ sᴇᴠ ᴅᴇ ʙɪʀᴀᴋɪᴘ ɢɪᴅᴇɴ ʏᴀʀ ᴜᴛᴀɴsɪɴ', 
'ᴏ ɢɪᴛᴛɪᴋᴛᴇɴ sᴏɴʀᴀ ɢᴇᴄᴇᴍ ɢᴜɴᴅᴜᴢᴇ ʜᴀsʀᴇᴛ ᴋᴀʟᴅɪ', 
'ʜᴇʀ sᴇʏɪɴ ʙɪᴛᴛɪɢɪ ʏᴇʀᴅᴇ ʙᴇɴᴅᴇ ʙɪᴛᴛɪᴍ ᴅᴇɢɪsᴛɪɴ ᴅɪʏᴇɴʟᴇʀɪɴ ᴇsɪʀɪʏɪᴍ', 
'ɢᴜᴠᴇɴᴍᴇᴋ  sᴇᴠᴍᴇᴋᴛᴇɴ ᴅᴀʜᴀ ᴅᴇɢᴇʀʟɪ , ᴢᴀᴍᴀɴʟᴀ ᴀɴʟᴀʀsɪɴ', 
'ɪɴsᴀɴ ʙᴀᴢᴇɴ ʙᴜʏᴜᴋ ʜᴀʏᴀʟʟᴇʀɪɴɪ ᴋᴜᴄᴜᴋ ɪɴsᴀɴʟᴀʀʟᴀ ᴢɪʏᴀɴ ᴇᴅᴇʀ', 
'ᴋɪᴍsᴇ ᴋɪᴍsᴇʏɪ ᴋᴀʏʙᴇᴛᴍᴇᴢ  ɢɪᴅᴇɴ ʙᴀsᴋᴀsɪɴɪ ʙᴜʟᴜʀ , ᴋᴀʟᴀɴ ᴋᴇɴᴅɪɴɪ', 
'ɢᴜᴄʟᴜ ɢᴏʀᴜɴᴇʙɪʟɪʀɪᴍ ᴀᴍᴀ ɪɴᴀɴ ʙᴀɴᴀ ʏᴏʀɢᴜɴᴜᴍ', 
'ᴏᴍʀᴜɴᴜᴢᴜ sᴜsᴛᴜᴋʟᴀʀɪɴɪᴢɪ ᴅᴜʏᴀɴ  ʙɪʀɪʏʟᴇ ɢᴇᴄɪʀɪɴ', 
'ʜᴀʏᴀᴛ ɪʟᴇʀɪʏᴇ ʙᴀᴋɪʟᴀʀᴀᴋ ʏᴀsᴀɴɪʀ ɢᴇʀɪʏᴇ ʙᴀᴋᴀʀᴀᴋ ᴀɴʟᴀsɪʟɪʀ', 
'ᴀʀᴛɪᴋ ʜɪᴄʙɪʀ sᴇʏ ᴇsᴋɪsɪ ɢɪʙɪ ᴅᴇɢɪʟ ʙᴜɴᴀ ʙᴇɴᴅᴇ ᴅᴀʜɪʟɪᴍ', 
'ᴋɪʏᴍᴇᴛ ʙɪʟᴇɴᴇ ɢᴏɴᴜʟᴅᴇ ᴠᴇʀɪʟɪʀ ᴏᴍᴜʀᴅᴇ', 
'ʙɪʀ ᴄɪᴄᴇᴋʟᴇ ɢᴜʟᴇʀ ᴋᴀᴅɪɴ , ʙɪʀ ʟᴀғʟᴀ ʜᴜᴢᴜɴ', 
'ᴋᴀʟʙɪ ɢᴜᴢᴇʟ ᴏʟᴀɴ ɪɴsᴀɴɪɴ ɢᴏᴢᴜɴᴅᴇɴ ʏᴀs ᴇᴋsɪᴋ ᴏʟᴍᴀᴢᴍɪs', 
'ʜᴇʀ sᴇʏɪ ʙɪʟᴇɴ ᴅᴇɢɪʟ ᴋɪʏᴍᴇᴛ ʙɪʟᴇɴ ɪɴsᴀɴʟᴀʀ ᴏʟsᴜɴ ʜᴀʏᴀᴛɪɴɪᴢᴅᴀ', 
'ᴍᴇsᴀғᴇ ɪʏɪᴅɪʀ ɴᴇ ʜᴀᴅᴅɪɴɪ ᴀsᴀɴ ᴏʟᴜʀ , ɴᴇ ᴅᴇ ᴄᴀɴɪɴɪ sɪᴋᴀɴ', 
'ʏᴜʀᴇɢɪᴍɪɴ ᴛᴀᴍ ᴏʀᴛᴀsɪɴᴅᴀ ʙᴜʏᴜᴋ ʙɪʀ ʏᴏʀɢᴜɴʟᴜᴋ ᴠᴀʀ', 
'ᴠᴇʀɪʟᴇɴ ᴅᴇɢᴇʀɪɴ ɴᴀɴᴋᴏʀᴜ ᴏʟᴍᴀʏɪɴ ɢᴇʀɪsɪ ʜᴀʟʟ ᴏʟᴜʀ', 
'ʜᴇᴍ ɢᴜᴄʟᴜ ᴏʟᴜᴘ ʜᴇᴍ ʜᴀssᴀs ᴋᴀʟᴘʟɪ ʙɪʀɪ ᴏʟᴍᴀᴋ ᴄᴏᴋ ᴢᴏʀ', 
'ᴍᴜʜᴛᴀᴄ ᴋᴀʟɪɴ ʏᴜʀᴇɢɪ ɢᴜᴢᴇʟ  ɪɴsᴀɴʟᴀʀᴀ', 
'ɪɴsᴀɴ ᴀɴʟᴀᴅɪɢɪ ᴠᴇ ᴀɴʟᴀsɪʟᴅɪɢɪ ɪɴsᴀɴᴅᴀ ᴄɪᴄᴇᴋ ᴀᴄᴀʀ', 
'ɪsᴛᴇʏᴇɴ ᴅᴀɢʟᴀʀɪ ᴀsᴀʀ ɪsᴛᴇᴍᴇʏᴇɴ ᴛᴜᴍsᴇɢɪ ʙɪʟᴇ ɢᴇᴄᴇᴍᴇᴢ', 
'ɪɴsᴀʟʟᴀʜ sᴀʙɪʀʟᴀ ʙᴇᴋʟᴇᴅɪɢɪɴ sᴇʏ ɪᴄɪɴ ʜᴀʏɪʀʟɪ ʙɪʀ ʜᴀʙᴇʀ ᴀʟɪʀsɪɴ', 
'ɪʏɪ ᴏʟᴀɴ ᴋᴀʏʙᴇᴛsᴇ ᴅᴇ ᴋᴀᴢᴀɴɪʀ', 
'ɢᴏɴʟᴜɴᴜᴢᴇ ᴀʟᴅɪɢɪɴɪᴢ , ɢᴏɴʟᴜɴᴜᴢᴜ ᴀʟᴍᴀʏɪ ʙɪʟsɪɴ', 
'ʏɪɴᴇ ʏɪʀᴛɪᴋ ᴄᴇʙɪᴍᴇ ᴋᴏʏᴍᴜsᴜᴍ ᴜᴍᴜᴅᴜᴍᴜ', 
'ᴏʟᴍᴇᴋ ʙɪʀ sᴇʏ ᴅᴇɢɪʟ ʏᴀsᴀᴍᴀᴋ ᴋᴏʀᴋᴜɴᴄ', 
'ɴᴇ ɪᴄɪᴍᴅᴇᴋɪ sᴏᴋᴀᴋʟᴀʀᴀ sɪɢᴀʙɪʟᴅɪᴍ ɴᴇ ᴅᴇ ᴅɪsᴀʀɪᴅᴀᴋɪ ᴅᴜɴʏᴀʏᴀ', 
'ɪɴsᴀɴ sᴇᴠɪʟᴍᴇᴋᴛᴇɴ ᴄᴏᴋ ᴀɴʟᴀsɪʟᴍᴀʏɪ ɪsᴛɪʏᴏʀᴅᴜ ʙᴇʟᴋɪ ᴅᴇ', 
'ᴇᴋᴍᴇᴋ ᴘᴀʜᴀʟɪ , ᴇᴍᴇᴋ ᴜᴄᴜᴢᴅᴜʀ', 
'sᴀᴠᴀsᴍᴀʏɪ ʙɪʀᴀᴋɪʏᴏʀᴜᴍ ʙᴜɴᴜ ᴠᴇᴅᴀ sᴀʏ'
    
    
)
    


@client.on(events.NewMessage(pattern="^/stag ?(.*)"))
async def stag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("𝖤𝗌𝗄𝗂 𝖬𝖾𝗌𝖺𝗃𝗅𝖺𝗋𝗂 𝖦𝗈𝗋𝖾𝗆𝗂𝗒𝗈𝗋𝗎𝗆 ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("• 𝖤𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝖬𝖾𝗌𝖺𝗃𝗂 𝖸𝖺𝗓𝗆𝖺𝖽𝗂𝗇 ! ")
  else:
    return await event.respond("• 𝖤𝗍𝗂𝗄𝖾𝗍 𝗂𝗌𝗅𝖾𝗆𝗂𝗇𝖾 𝖻𝖺𝗌𝗅𝖺𝗆𝖺𝗆 𝗂𝖼𝗂𝗇 𝖻𝗂𝗋 𝗌𝖾𝖻𝖾𝗉 𝗒𝖺𝗓𝗂𝗇 ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "• merdobey 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝗅𝖺ttı . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(soz)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ merdobey 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖽𝗎𝗋𝖽urdu . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} \n {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    
#########################

# renk ile etiketleme modülü
renk = "🦓 🐅 🐈‍⬛ 🐄 🦄 🐇 🐁 🐷 🐶 🙈 🙊 🐻 🐼 🦊 🐮 🐍 🐊 🦨 🦔 🐒 🦣 🦘 🦥 🦦 🦇 🦍 🐥 🐦 🦜 🕊️ 🦤 🦢 🦩 🦚 🦃 🐣 🐓 🐬 🦈 🐠 🐳 🦗 🪳 🐝 🐞 🦋 🐟 🕷️ 🦑 " .split(" ") 
        

@client.on(events.NewMessage(pattern="^/mtag ?(.*)"))
async def rtag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("** Eski mesajları göremiyorum !**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**• Etiketleme mesajı yazmadın !**")
  else:
    return await event.respond("**• Etiketleme için bir mesaj yazın !**")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "✅ merdobey 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖻𝖺𝗌𝗅𝖺ttı . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/support')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(renk)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ merdobey 𝖾𝗍𝗂𝗄𝖾𝗍𝗅𝖾𝗆𝖾 𝗂𝗌𝗅𝖾𝗆𝗂 𝖽𝗎𝗋durdu .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  )
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt} \n {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


###


print(">> Bot çalışmaktadir merak etme 🚀 @tMertTt bilgi alabilirsin <<")
client.run_until_disconnected()
run_until_disconnected()
