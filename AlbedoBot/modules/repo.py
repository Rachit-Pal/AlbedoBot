from telethon import Button

from AlbedoBot import tbot as tbot
from AlbedoBot.events import register

PHOTO = "https://telegra.ph/file/dfab6719178ae1c893f63.jpg"


@register(pattern=("/repo"))
async def awake(event):
    NEKO = """
         We Are So Happy To Announce That We Have Public Our AlbedoBot Repo. π
βββββββββββββ
γ@DarkAlbedoBotγ
βββββββββββββ
Here is the Repo Deploy your Own AlbedoBot.
βοΈRepo β€ https://github.com/Rachit-Pal/AlbedoBot.git
βββββββββββββ
π° Thanks for your support 
It's Fully stable Repo so you can deploy and make own Bot.
ββββββββββββββββββ
Powered By:- @SAlTAM4
"""

    BUTTON = [
        [
            Button.url("π Repository", "https://github.com/Rachit-Pal/AlbedoBot"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO, buttons=BUTTON)
