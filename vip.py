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
vip_tag = []


  
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
                       Button.url('📝  channel  ', f'https://t.me/katil_bots')]
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
  global vip_tag
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
    vip_tag.append(event.chat_id)
    usernum = 0
    usertxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usernum += 1
      usertxt += f"[{usr.first_name}](tg://user?id={usr.id}) , "
      if event.chat_id not in vip_tag:
        await event.respond("⛔ your action stop . . .",
                    buttons=(
                      [
                       Button.url('📝  channel  📝', f'https://t.me/katil_bots')
                      ]
                    )
                  )
        return
      if usernum == 5:
        await client.send_message(event.chat_id, f"{msg} \n {usrtxt}")
        await asyncio.sleep(2)
        usernum = 0
        usertxt = ""

    

#########################

# admin tagging modules
@client.on(events.NewMessage(pattern="^/atag ?(.*)"))
async def mentionalladmin(event):
  global vip_tag
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
    vip_tag.append(event.chat_id)
    usernum = 0
    usertxt = ""
    async for user in client.iter_participants(event.chat_id):
      usernum += 1
      usertxt += f"• [{user.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in vip_tag:
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
  global vip_tag
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
    vip_tag.append(event.chat_id)
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
  global vip_tag
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
    vip_tag.append(event.chat_id)
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
" 🌺**बहुत अच्छा लगता है तुझे सताना और फिर प्यार से तुझे मनाना।**🌺 \n\n**🥀Bahut aacha lagta hai tujhe satana Aur fir pyar se tujhe manana.🥀** ",
" 🌺**मेरी जिंदगी मेरी जान हो तुम मेरे सुकून का दुसरा नाम हो तुम।**🌺 \n\n**🥀Meri zindagi Meri jaan ho tum Mere sukoon ka Dusra naam ho tum.🥀** ",
" 🌺**तुम मेरी वो खुशी हो जिसके बिना, मेरी सारी खुशी अधूरी लगती है।**🌺 \n\n**🥀**Tum Meri Wo Khushi Ho Jiske Bina, Meri Saari Khushi Adhuri Lagti Ha.🥀** ",
" 🌺**काश वो दिन जल्दी आए,जब तू मेरे साथ सात फेरो में बन्ध जाए।**🌺 \n\n**🥀Kash woh din jldi aaye Jb tu mere sath 7 feron me bndh jaye.🥀** ",
" 🌺**अपना हाथ मेरे दिल पर रख दो और अपना दिल मेरे नाम कर दो।**🌺 \n\n**🥀apna hath mere dil pr rakh do aur apna dil mere naam kar do.🥀** ",
" 🌺**महादेव ना कोई गाड़ी ना कोई बंगला चाहिए सलामत रहे मेरा प्यार बस यही दुआ चाहिए।**🌺 \n\n**🥀Mahadev na koi gadi na koi bangla chahiye salamat rhe mera pyar bas yahi dua chahiye.🥀** ",
" 🌺**फिक्र तो होगी ना तुम्हारी इकलौती मोहब्बत हो तुम मेरी।**🌺 \n\n**🥀Fikr to hogi na tumhari ikloti mohabbat ho tum meri.🥀** ",
" 🌺**सुनो जानू आप सिर्फ किचन संभाल लेना आप को संभालने के लिए मैं हूं ना।**🌺 \n\n**🥀suno jaanu aap sirf kitchen sambhal lena ap ko sambhlne ke liye me hun naa.🥀** ",
" 🌺**सौ बात की एक बात मुझे चाहिए बस तेरा साथ।**🌺 \n\n**🥀So bat ki ek bat mujhe chahiye bas tera sath.🥀** ",
" 🌺**बहुत मुश्किलों से पाया हैं तुम्हें, अब खोना नहीं चाहते,कि तुम्हारे थे तुम्हारे हैं अब किसी और के होना नहीं चाहते।**🌺 \n\n**🥀Bahut muskilon se paya hai tumhe Ab khona ni chahte ki tumhare they tumhare hai ab kisi or k hona nhi chahte.🥀** ",
" 🌺**बेबी बातें तो रोज करते है चलो आज रोमांस करते है।**🌺 \n\n**🥀Baby baten to roj karte haichalo aaj romance karte hai..🥀** ",
" 🌺**सुबह शाम तुझे याद करते है हम और क्या बताएं की तुमसे कितना प्यार करते है हम।**🌺 \n\n**🥀subha sham tujhe yad karte hai hum aur kya batayen ki tumse kitna pyar karte hai hum.🥀** ",
" 🌺**किसी से दिल लग जाने को मोहब्बत नहीं कहते जिसके बिना दिल न लगे उसे मोहब्बत कहते हैं।**🌺 \n\n**🥀Kisi se dil lag jane ko mohabbat nahi kehte jiske nina dil na lage use mohabbat kehte hai.🥀** ",
" 🌺**मेरे दिल के लॉक की चाबी हो तुम क्या बताएं जान मेरे जीने की एकलौती वजह हो तुम।**🌺 \n\n**🥀mere dil ke lock ki chabi ho tum kya batayen jaan mere jeene ki eklauti wajah ho tum..🥀** ",
" 🌺**हम आपकी हर चीज़ से प्यार कर लेंगे, आपकी हर बात पर ऐतबार कर लेंगे, बस एक बार कह दो कि तुम सिर्फ मेरे हो, हम ज़िन्दगी भर आपका इंतज़ार कर लेंगे।**🌺 \n\n**🥀Hum apki har cheez se pyar kar lenge apki har baat par etvar kar lenge bas ek bar keh do ki tum sirf mere ho hum zindagi bhar apka intzaar kar lenge..🥀** ",
" 🌺**मोहब्बत कभी स्पेशल लोगो से नहीं होती जिससे होती है वही स्पेशल बन जाता है।**🌺 \n\n**🥀Mohabbat kabhi special logo se nahi hoti jisse bhi hoti hai wahi special ban jate hai,.🥀**",
" 🌺**तू मेरी जान है इसमें कोई शक नहीं तेरे अलावा मुझ पर किसी और का हक़ नहीं।**🌺 \n\n**🥀Tu meri jaan hai isme koi shak nahi tere alawa mujhe par kisi aur ka hak nhi..🥀** ",
" 🌺**पहली मोहब्बत मेरी हम जान न सके, प्यार क्या होता है हम पहचान न सके, हमने उन्हें दिल में बसा लिया इस कदर कि, जब चाहा उन्हें दिल से निकाल न सके।**🌺 \n\n**🥀Pehli mohabbat meri hum jaan na sake pyar kya hota hai hum pehchan na sake humne unhe dil me basa liya is kadar ki jab chaha unhe dil se nikal na sake.🥀** ",
" 🌺**खुद नहीं जानती वो कितनी प्यारी हैं , जान है हमारी पर जान से प्यारी हैं, दूरियों के होने से कोई फर्क नहीं पड़ता वो कल भी हमारी थी और आज भी हमारी है.**🌺 \n\n**🥀khud nahi janti vo kitni pyari hai jan hai hamari par jan se jyda payari hai duriya ke hone se frak nahi pdta vo kal bhe hamari the or aaj bhe hamari hai.🥀** ",
" 🌺**चुपके से आकर इस दिल में उतर जाते हो, सांसों में मेरी खुशबु बनके बिखर जाते हो, कुछ यूँ चला है तेरे इश्क का जादू, सोते-जागते तुम ही तुम नज़र आते हो।**🌺 \n\n**🥀Chupke Se Aakar Iss Dil Mein Utar Jate Ho, Saanso Mein Meri Khushbu BanKe Bikhar Jate Ho,Kuchh Yun Chala Hai Tere Ishq Ka Jadoo, Sote-Jagte Tum Hi Tum Najar Aate Ho..🥀** ",
" 🌺**प्यार करना सिखा है नफरतो का कोई ठौर नही, बस तु ही तु है इस दिल मे दूसरा कोई और नही.**🌺 \n\n**🥀Pyar karna sikha hai naftaro ka koi thor nahi bas tu hi tu hai is dil me dusra koi aur nahi hai.🥀** ",
" 🌺**रब से आपकी खुशीयां मांगते है, दुआओं में आपकी हंसी मांगते है, सोचते है आपसे क्या मांगे,चलो आपसे उम्र भर की मोहब्बत मांगते है।**🌺\n\n**🥀Rab se apki khushiyan mangte hai duao me apki hansi mangte hai sochte hai apse kya mange chalo apse umar bhar ki mohabbat mangte hai..🥀** ",
" 🌺**काश मेरे होंठ तेरे होंठों को छू जाए देखूं जहा बस तेरा ही चेहरा नज़र आए हो जाए हमारा रिश्ता कुछ ऐसा होंठों के साथ हमारे दिल भी जुड़ जाए.**🌺\n\n**🥀kash mere hoth tere hontho ko chu jayen dekhun jaha bas teri hi chehra nazar aaye ho jayen humara rishta kuch easa hothon ke sath humare dil bhi jud jaye.🥀** ",
" 🌺**आज मुझे ये बताने की इजाज़त दे दो, आज मुझे ये शाम सजाने की इजाज़त दे दो, अपने इश्क़ मे मुझे क़ैद कर लो,आज जान तुम पर लूटाने की इजाज़त दे दो.**🌺\n\n**🥀Aaj mujhe ye batane ki izazat de do, aaj mujhe ye sham sajane ki izazat de do, apne ishq me mujhe ked kr lo aaj jaan tum par lutane ki izazat de do..🥀** ",
" 🌺**जाने लोग मोहब्बत को क्या क्या नाम देते है, हम तो तेरे नाम को ही मोहब्बत कहते है.**🌺\n\n**🥀Jane log mohabbat ko kya kya naam dete hai hum to tere naam ko hi mohabbat kehte hai..🥀** ",
" 🌺**देख के हमें वो सिर झुकाते हैं। बुला के महफिल में नजर चुराते हैं। नफरत हैं हमसे तो भी कोई बात नहीं। पर गैरो से मिल के दिल क्यों जलाते हो।**🌺\n\n**🥀Dekh Ke Hame Wo Sir Jhukate Hai Bula Ke Mahfhil Me Najar Churate Hai Nafrat Hai Hamse To Bhi Koei Bat Nhi Par Gairo Se Mil Ke Dil Kyo Jalate Ho.🥀** ",
" 🌺**तेरे बिना टूट कर बिखर जायेंगे,तुम मिल गए तो गुलशन की तरह खिल जायेंगे, तुम ना मिले तो जीते जी ही मर जायेंगे, तुम्हें जो पा लिया तो मर कर भी जी जायेंगे।**🌺\n\n**🥀Tere bina tut kar bikhar jeynge tum mil gaye to gulshan ki tarha khil jayenge tum na mile to jite ji hi mar jayenge tumhe jo pa liya to mar kar bhi ji jayenge..🥀** ",
" 🌺**सनम तेरी कसम जेसे मै जरूरी हूँ तेरी ख़ुशी के लिये, तू जरूरी है मेरी जिंदगी के लिये.**🌺\n\n**🥀Sanam teri kasam jese me zaruri hun teri khushi ke liye tu zaruri hai meri zindagi ke liye.🥀** ",
" 🌺**तुम्हारे गुस्से पर मुझे बड़ा प्यार आया हैं इस बेदर्द दुनिया में कोई तो हैं जिसने मुझे पुरे हक्क से धमकाया हैं.**🌺\n\n**🥀Tumharfe gusse par mujhe pyar aaya hai is bedard duniya me koi to hai jisne mujhe pure hakk se dhamkaya hai.🥀** ",
" 🌺**पलको से आँखो की हिफाजत होती है धडकन दिल की अमानत होती है ये रिश्ता भी बडा प्यारा होता है कभी चाहत तो कभी शिकायत होती है.**🌺\n\n**🥀Palkon se Aankho ki hifajat hoti hai dhakad dil ki Aamanat hoti hai, ye rishta bhi bada pyara hota hai, kabhi chahat to kabhi shikayat hoti hai.🥀** ",
" 🌺**मुहब्बत को जब लोग खुदा मानते हैं प्यार करने वाले को क्यों बुरा मानते हैं। जब जमाना ही पत्थर दिल हैं। फिर पत्थर से लोग क्यों दुआ मांगते है।**🌺\n\n**🥀Muhabbt Ko Hab Log Khuda Mante Hai, Payar Karne Walo Ko Kyu Bura Mante Hai,Jab Jamana Hi Patthr Dil Hai,Fhir Patthr Se Log Kyu Duaa Magte Hai.🥀** ",
" 🌺**हुआ जब इश्क़ का एहसास उन्हें आकर वो पास हमारे सारा दिन रोते रहे हम भी निकले खुदगर्ज़ इतने यारो कि ओढ़ कर कफ़न, आँखें बंद करके सोते रहे।**🌺\n\n**🥀Hua jab ishq ka ehsaas unhe akar wo pass humare sara din rate rahe, hum bhi nikale khudgarj itne yaro ki ood kar kafan ankhe band krke sote rhe.🥀** ",
" 🌺**दिल के कोने से एक आवाज़ आती हैं। हमें हर पल उनकी याद आती हैं। दिल पुछता हैं बार -बार हमसे के जितना हम याद करते हैं उन्हें क्या उन्हें भी हमारी याद आती हैं।**🌺\n\n**🥀Dil Ke Kone Se Ek Aawaj Aati Hai, Hame Har Pal Uaski Yad Aati Hai, Dil Puchhta Hai Bar Bar Hamse Ke, Jitna Ham Yad Karte Hai Uanhe, Kya Uanhe Bhi Hamari Yad Aati Hai,🥀** ",
" 🌺**कभी लफ्ज़ भूल जाऊं कभी बात भूल जाऊं, तूझे इस कदर चाहूँ कि अपनी जात भूल जाऊं, कभी उठ के तेरे पास से जो मैं चल दूँ, जाते हुए खुद को तेरे पास भूल जाऊं।**🌺\n\n**🥀Kabhi Lafz Bhool Jaaun Kabhi Baat Bhool Jaaun, Tujhe Iss Kadar Chahun Ki Apni Jaat Bhool Jaaun, Kabhi Uthh Ke Tere Paas Se Jo Main Chal Dun, Jaate Huye Khud Ko Tere Paas Bhool Jaaun..🥀** ",
" 🌺**आईना देखोगे तो मेरी याद आएगी साथ गुज़री वो मुलाकात याद आएगी पल भर क लिए वक़्त ठहर जाएगा, जब आपको मेरी कोई बात याद आएगी.**🌺\n\n**🥀Aaina dekhoge to meri yad ayegi sath guzari wo mulakat yad ayegi pal bhar ke waqt thahar jayega jab apko meri koi bat yad ayegi.🥀** ",
" 🌺**प्यार किया तो उनकी मोहब्बत नज़र आई दर्द हुआ तो पलके उनकी भर आई दो दिलों की धड़कन में एक बात नज़र आई दिल तो उनका धड़का पर आवाज़ इस दिल की आई.**🌺\n\n**🥀Pyar kiya to unki mohabbat nazar aai dard hua to palke unki bhar aai do dilon ki dhadkan me ek baat nazar aai dil to unka dhadka par awaz dil ki aai.🥀** ",
" 🌺**कई चेहरे लेकर लोग यहाँ जिया करते हैं हम तो बस एक ही चेहरे से प्यार करते हैं ना छुपाया करो तुम इस चेहरे को,क्योंकि हम इसे देख के ही जिया करते हैं.**🌺\n\n**🥀Kai chehre lekar log yahn jiya karte hai hum to bas ek hi chehre se pyar karte hai na chupaya karo tum is chehre ko kyuki hum ise dekh ke hi jiya karte hai.🥀** ",
" 🌺**सबके bf को अपनी gf से बात करके नींद आजाती है और मेरे वाले को मुझसे लड़े बिना नींद नहीं आती।**🌺\n\n**🥀Sabke bf ko apni gf se baat karke nind aajati hai aur mere wale ko mujhse lade bina nind nhi aati.🥀** ",
" 🌺**सच्चा प्यार कहा किसी के नसीब में होता है. एसा प्यार कहा इस दुनिया में किसी को नसीब होता है.**🌺\n\n**🥀Sacha pyar kaha kisi ke nasib me hota hai esa pyar kahan is duniya me kisi ko nasib hota hai.🥀** "
    
    
)
    


@client.on(events.NewMessage(pattern="^/stag ?(.*)"))
async def stag(event):
  global vip_tag
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
    vip_tag.append(event.chat_id)
    usernum = 0
    usertxt = ""
    async for user in client.iter_participants(event.chat_id):
      usernum += 1
      usertxt += f"[{random.choice(srt)}](tg://user?id={user.id}) "
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

# colour tag module
colour = "🦓 🐅 🐈‍⬛ 🐄 🦄 🐇 🐁 🐷 🐶 🙈 🙊 🐻 🐼 🦊 🐮 🐍 🐊 🦨 🦔 🐒 🦣 🦘 🦥 🦦 🦇 🦍 🐥 🐦 🦜 🕊️ 🦤 🦢 🦩 🦚 🦃 🐣 🐓 🐬 🦈 🐠 🐳 🦗 🪳 🐝 🐞 🦋 🐟 🕷️ 🦑 " .split(" ") 
        

@client.on(events.NewMessage(pattern="^/mtag ?(.*)"))
async def rtag(event):
  global vip_tag
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
    vip_tag.append(event.chat_id)
    usernum = 0
    usertxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usernum += 1
      usertxt += f"[{random.choice(colour)}](tg://user?id={user.id}) "
      if event.chat_id not in vip_tag:
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
