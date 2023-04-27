#katil#
import random
import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation
from config import client, USERNAME, log_group, startmessage, groupstart, commands, owner, support
import heroku3
import random
import asyncio
import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation
from pyrogram import Client 
from pyrogram import filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from random import randint
from time import sleep




logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)



anlik_calisan = []
etiket_tagger = []

  
#onetag
@client.on(events.NewMessage(pattern="^/start$"))
async def cancel(event):
  global etiket_tagger
  etiket_tagger.remove(event.chat_id)

    
# start message 
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for user in client.iter_participants(event.chat_id):
     ad = f"• HELLO [{user.first_name}](tg://user?id={user.id}) "
     await client.send_message(log_group, f"ℹ️ **New User -** \n {ad}")
     return await event.reply(f"{ad} {startmessage}", buttons=(
                      [
                       Button.url('🎉  add me in your group  🎉', f'https://t.me/{USERNAME}?startgroup=true')],
                      [
                       Button.inline("📚  commands  ", data="commands"),
                       Button.url('👨‍💻  𝖮𝗐𝗇𝖾𝗋  ', f'https://t.me/katil_your_dad')],
                       [Button.url('📝  support  ', f'https://t.me/{support}')]
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"{groupstart}")

# Start Button
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for user in client.iter_participants(event.chat_id):
     ad = f"• HELLO [{user.first_name}](tg://user?id={user.id}) "
     await event.edit(f"{ad} {startmessage}", buttons=(
                      [
                       Button.url('🎉  add me in your group  🎉', f'https://t.me/{USERNAME}?startgroup=true')],
                      [Button.inline("📚  commands  ", data="commands"),
                       Button.url('👨‍💻  𝖮𝗐𝗇𝖾𝗋  ', f'https://t.me/katil_your_dad')]
                       [Button.url('📝  channel  ', f'https://t.me/katil_bots')]
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

# 5 member tag modules
@client.on(events.NewMessage(pattern="^/utag ?(.*)"))
async def mentionall(event):
  global etiket_tagger
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
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
        return await event.respond("i can't see old messages ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("• you didn't write tagging message ! ")
  else:
    return await event.respond("• give me a reason to start the tag process ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "✅member tagging process started . . .",
                    buttons=(
                      [
                      Button.url('📝  channel  📝', f'https://t.me/katil_bots')
                      ]
                    )
                  ) 
    etiket_tagger.append(event.chat_id)
    usernum = 0
    usertxt = ""
    async for user in client.iter_participants(event.chat_id):
      usernum += 1
      usertxt += f"[{user.first_name}](tg://user?id={user.id}) , "
      if event.chat_id not in etiket_tagger:
        await event.respond("⛔ your action stop . . .",
                    buttons=(
                      [
                       Button.url('📝  channel  📝', f'https://t.me/katil_bots')
                      ]
                    )
                  )
        return
      if usernum == 5:
        await client.send_message(event.chat_id, f"{msg} \n {usertxt}")
        await asyncio.sleep(2)
        usernum = 0
        usertxt = ""

    

#########################

# admin tagging modules
@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global etiket_tagger
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
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
        return await event.respond("i can't see old messages ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("• you didn't write a tagging message ! ")
  else:
    return await event.respond("• give me a reason to start the tag process ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "✅admin tagging process started . . .",
                    buttons=(
                      [
                       Button.url('📝  channel  📝', f'https://t.me/katil_bots')
                      ]
                    )
                  ) 
    etiket_tagger.append(event.chat_id)
    usernum = 0
    usertxt = ""
    async for user in client.iter_participants(event.chat_id):
      usernum += 1
      usertxt += f"• [{user.first_name}](tg://user?id={user.id}) "
      if event.chat_id not in etiket_tagger:
        await event.respond("⛔ tagging stopped . . .",
                    buttons=(
                      [
                       Button.url('📝  channel  📝', f'https://t.me/katil_bots')
                      ]
                    )
                  )
        return
      if usernum == 1:
        await client.send_message(event.chat_id, f"{usertxt} \n {msg}")
        await asyncio.sleep(2)
        usernum = 0
        usertxt = ""

    

#########################

# one by one tagging module
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def onlytag(event):
  global etiket_tagger
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
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
        return await event.respond("i can't see old messages ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("• you didn't write a tagging message ! ")
  else:
    return await event.respond("• write a reason to start the tag process ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "✅ tagging process started . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  ) 
    etiket_tagger.append(event.chat_id)
    usernum = 0
    usertxt = ""
    async for user in client.iter_participants(event.chat_id):
      usernum += 1
      usertxt += f"• [{user.first_name}](tg://user?id={user.id}) "
      if event.chat_id not in vip_tag:
        await event.respond("⛔ tagging has stopped . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  )
        return
      if usernum == 1:
        await client.send_message(event.chat_id, f"{usertxt} \n {msg}")
        await asyncio.sleep(2)
        usernum = 0
        usertxt = ""

    

#########################

# Emoji tag module

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
  global etiket_tagger
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
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
        return await event.respond("i can't see old messages ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("• you didn't write a tagging message ! ")
  else:
    return await event.respond("• write a reason to start the tag process ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "✅ tagging process started . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  ) 
    etiket_tagger.append(event.chat_id)
    usernum = 0
    usertxt = ""
    async for user in client.iter_participants(event.chat_id):
      usernum += 1
      usertxt += f"[{random.choice(emoji)}](tg://user?id={user.id}) , "
      if event.chat_id not in vip_tag:
        await event.respond("⛔ tagging has stopped . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  )
        return
      if usernum == 5:
        await client.send_message(event.chat_id, f"{usertxt} \n {msg}")
        await asyncio.sleep(2)
        usernum = 0
        usertxt = ""

    

#########################

# srt tag module

srt = (
'🥀Bahut aacha lagta hai tujhe satana Aur fir pyar se tujhe manana.🥀',
'🥀Meri zindagi Meri jaan ho tum Mere sukoon ka Dusra naam ho tum.🥀',
'🥀Tum Meri Wo Khushi Ho Jiske Bina, Meri Saari Khushi Adhuri Lagti Ha.🥀',
'🥀Kash woh din jldi aaye Jb tu mere sath 7 feron me bndh jaye.🥀',
'🥀apna hath mere dil pr rakh do aur apna dil mere naam kar do.🥀',
'🥀Mahadev na koi gadi na koi bangla chahiye salamat rhe mera pyar bas yahi dua chahiye.🥀',
'🥀Fikr to hogi na tumhari ikloti mohabbat ho tum meri.🥀',
'🥀suno jaanu aap sirf kitchen sambhal lena ap ko sambhlne ke liye me hun naa.🥀',
'🥀So bat ki ek bat mujhe chahiye bas tera sath.🥀',
'🥀Bahut muskilon se paya hai tumhe Ab khona ni chahte ki tumhare they tumhare hai ab kisi or k hona nhi chahte.🥀',
'🥀Baby baten to roj karte haichalo aaj romance karte hai..🥀',
'🥀subha sham tujhe yad karte hai hum aur kya batayen ki tumse kitna pyar karte hai hum.🥀',
'🥀Kisi se dil lag jane ko mohabbat nahi kehte jiske nina dil na lage use mohabbat kehte hai.🥀',
'🥀mere dil ke lock ki chabi ho tum kya batayen jaan mere jeene ki eklauti wajah ho tum..🥀',
'🥀Hum apki har cheez se pyar kar lenge apki har baat par etvar kar lenge bas ek bar keh do ki tum sirf mere ho hum zindagi bhar apka intzaar kar lenge..🥀',
'🥀Mohabbat kabhi special logo se nahi hoti jisse bhi hoti hai wahi special ban jate hai,.🥀',
'🥀Tu meri jaan hai isme koi shak nahi tere alawa mujhe par kisi aur ka hak nhi..🥀',
'🥀Pehli mohabbat meri hum jaan na sake pyar kya hota hai hum pehchan na sake humne unhe dil me basa liya is kadar ki jab chaha unhe dil se nikal na sake.🥀',
'🥀khud nahi janti vo kitni pyari hai jan hai hamari par jan se jyda payari hai duriya ke hone se frak nahi pdta vo kal bhe hamari the or aaj bhe hamari hai.🥀',
'🥀Chupke Se Aakar Iss Dil Mein Utar Jate Ho, Saanso Mein Meri Khushbu BanKe Bikhar Jate Ho,Kuchh Yun Chala Hai Tere Ishq Ka Jadoo, Sote-Jagte Tum Hi Tum Najar Aate Ho..🥀',
'🥀Pyar karna sikha hai naftaro ka koi thor nahi bas tu hi tu hai is dil me dusra koi aur nahi hai.🥀',
'🥀Rab se apki khushiyan mangte hai duao me apki hansi mangte hai sochte hai apse kya mange chalo apse umar bhar ki mohabbat mangte hai..🥀',
'🥀kash mere hoth tere hontho ko chu jayen dekhun jaha bas teri hi chehra nazar aaye ho jayen humara rishta kuch easa hothon ke sath humare dil bhi jud jaye.🥀',
'🥀Aaj mujhe ye batane ki izazat de do, aaj mujhe ye sham sajane ki izazat de do, apne ishq me mujhe ked kr lo aaj jaan tum par lutane ki izazat de do..🥀',
'🥀Jane log mohabbat ko kya kya naam dete hai hum to tere naam ko hi mohabbat kehte hai..🥀',
'🥀Dekh Ke Hame Wo Sir Jhukate Hai Bula Ke Mahfhil Me Najar Churate Hai Nafrat Hai Hamse To Bhi Koei Bat Nhi Par Gairo Se Mil Ke Dil Kyo Jalate Ho.🥀',
'🥀Tere bina tut kar bikhar jeynge tum mil gaye to gulshan ki tarha khil jayenge tum na mile to jite ji hi mar jayenge tumhe jo pa liya to mar kar bhi ji jayenge..🥀',
'🥀Sanam teri kasam jese me zaruri hun teri khushi ke liye tu zaruri hai meri zindagi ke liye.🥀',
'🥀Tumharfe gusse par mujhe pyar aaya hai is bedard duniya me koi to hai jisne mujhe pure hakk se dhamkaya hai.🥀',
'🥀Palkon se Aankho ki hifajat hoti hai dhakad dil ki Aamanat hoti hai, ye rishta bhi bada pyara hota hai, kabhi chahat to kabhi shikayat hoti hai.🥀',
'🥀Muhabbt Ko Hab Log Khuda Mante Hai, Payar Karne Walo Ko Kyu Bura Mante Hai,Jab Jamana Hi Patthr Dil Hai,Fhir Patthr Se Log Kyu Duaa Magte Hai.🥀',
'🥀Hua jab ishq ka ehsaas unhe akar wo pass humare sara din rate rahe, hum bhi nikale khudgarj itne yaro ki ood kar kafan ankhe band krke sote rhe.🥀',
'🥀Dil Ke Kone Se Ek Aawaj Aati Hai, Hame Har Pal Uaski Yad Aati Hai, Dil Puchhta Hai Bar Bar Hamse Ke, Jitna Ham Yad Karte Hai Uanhe, Kya Uanhe Bhi Hamari Yad Aati Hai,🥀',
'🥀Kabhi Lafz Bhool Jaaun Kabhi Baat Bhool Jaaun, Tujhe Iss Kadar Chahun Ki Apni Jaat Bhool Jaaun, Kabhi Uthh Ke Tere Paas Se Jo Main Chal Dun, Jaate Huye Khud Ko Tere Paas Bhool Jaaun..🥀',
'🥀Aaina dekhoge to meri yad ayegi sath guzari wo mulakat yad ayegi pal bhar ke waqt thahar jayega jab apko meri koi bat yad ayegi.🥀',
'🥀Pyar kiya to unki mohabbat nazar aai dard hua to palke unki bhar aai do dilon ki dhadkan me ek baat nazar aai dil to unka dhadka par awaz dil ki aai.🥀',
'🥀Kai chehre lekar log yahn jiya karte hai hum to bas ek hi chehre se pyar karte hai na chupaya karo tum is chehre ko kyuki hum ise dekh ke hi jiya karte hai.🥀',
'🥀Sabke bf ko apni gf se baat karke nind aajati hai aur mere wale ko mujhse lade bina nind nhi aati.🥀',
'🥀Sacha pyar kaha kisi ke nasib me hota hai esa pyar kahan is duniya me kisi ko nasib hota hai.🥀'
    
    
)
    


@client.on(events.NewMessage(pattern="^/stag ?(.*)"))
async def stag(event):
  global etiket_tagger
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
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
        return await event.respond("i can't see old messages ! ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("• you didn't write a tagging message ! ")
  else:
    return await event.respond("• write a reason to start the tag process ! ")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "• tagging process started . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  ) 
    etiket_tagger.append(event.chat_id)
    usernum = 0
    usertxt = ""
    async for user in client.iter_participants(event.chat_id):
      usernum += 1
      usertxt += f"[{random.choice(srt)}](tg://user?id={user.id}) "
      if event.chat_id not in etiket_tagger:
        await event.respond("⛔ tagging has stopped . . .",
                    buttons=(
                      [
                       Button.url('📝  channel  📝', f'https://t.me/katil_bots')
                      ]
                    )
                  )
        return
      if usernum == 1:
        await client.send_message(event.chat_id, f"{usertxt} \n {msg}")
        await asyncio.sleep(2)
        usernum = 0
        usertxt = ""

    
#########################

# colour tag module
colour = "🦓 🐅 🐈‍⬛ 🐄 🦄 🐇 🐁 🐷 🐶 🙈 🙊 🐻 🐼 🦊 🐮 🐍 🐊 🦨 🦔 🐒 🦣 🦘 🦥 🦦 🦇 🦍 🐥 🐦 🦜 🕊️ 🦤 🦢 🦩 🦚 🦃 🐣 🐓 🐬 🦈 🐠 🐳 🦗 🪳 🐝 🐞 🦋 🐟 🕷️ 🦑 " .split(" ") 
        

@client.on(events.NewMessage(pattern="^/mtag ?(.*)"))
async def rtag(event):
  global etiket_tagger
  if event.is_private:
    return await event.respond(f"{nogroup}")
  
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
        return await event.respond("** i can't see old messages !**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**• you didn't write a tagging message !**")
  else:
    return await event.respond("**• write a message for tagging !**")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "✅ tagging process started . . .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  ) 
    etiket_tagger.append(event.chat_id)
    usernum = 0
    usertxt = ""
    async for user in client.iter_participants(event.chat_id):
      usernum += 1
      usertxt += f"[{random.choice(colour)}](tg://user?id={user.id}) "
      if event.chat_id not in etiket_tagger:
        await event.respond("⛔ tagging has stopped .",
                    buttons=(
                      [
                       Button.url('📝  support  📝', f'https://t.me/katilsupport')
                      ]
                    )
                  )
        return
      if usernum == 5:
        await client.send_message(event.chat_id, f"{usertxt} \n {msg}")
        await asyncio.sleep(2)
        usernum = 0
        usertxt = ""


###


print(">> Bot is working don't worry 🚀 join @katil_bots you can get information here <<")
client.run_until_disconnected()
run_until_disconnected()
