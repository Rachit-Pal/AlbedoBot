from telethon import Button

from AlbedoBot import tbot as tbot
from AlbedoBot.events import register

PHOTO = "https://telegra.ph/file/dfab6719178ae1c893f63.jpg"


@register(pattern=("/repo"))
async def awake(event):
    NEKO = """
         We Are So Happy To Announce That We Have Public Our AlbedoBot Repo. 💟
➖➖➖➖➖➖➖➖➖➖➖➖➖
「@DarkAlbedoBot」
➖➖➖➖➖➖➖➖➖➖➖➖➖
Here is the Repo Deploy your Own AlbedoBot.
⚜️Repo ➤ https://github.com/Rachit-Pal/AlbedoBot.git
➖➖➖➖➖➖➖➖➖➖➖➖➖
🔰 Thanks for your support 
It's Fully stable Repo so you can deploy and make own Bot.
──────────────────
Powered By:- @SAlTAM4
"""

    BUTTON = [
        [
            Button.url("🎛 Repository", "https://github.com/Rachit-Pal/AlbedoBot"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
