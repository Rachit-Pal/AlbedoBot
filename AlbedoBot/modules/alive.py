import asyncio
import datetime
from datetime import datetime

from pyrogram import __version__ as pyrover
from telethon import Button
from telethon import __version__ as tlhver

from AlbedoBot import BOT_NAME, BOT_USERNAME
from AlbedoBot import tbot as neko
from AlbedoBot.events import register

edit_time = 5
""" =======================Neko====================== """
file1 = "https://telegra.ph/file/cd7aad1ea310312886358.png"
file2 = "https://telegra.ph/file/48a97320463caa61dba3d.png"
file3 = "https://telegra.ph/file/2295a7207495eccbbe298.png"
file4 = "https://telegra.ph/file/67e0bf231a97cd2e364ea.png"
file5 = "https://telegra.ph/file/990684ecd3d119fa9fec6.png"
""" =======================Neko====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@register(pattern=("/alive"))
async def hmm(yes):
    await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    NekoX = f"** ♡ Hey [{yes.sender.first_name}](tg://user?id={yes.sender.id}) I'm {BOT_NAME} **\n\n"
    NekoX += f"**♡ My Uptime :** `{uptime}`\n\n"
    NekoX += f"**♡ Python Version :** `{python_version}`\n\n"
    NekoX += f"**♡ Telethon Version :** `{tlhver}`\n\n"
    NekoX += f"**♡ Pyrogram Version :** `{pyrover}`\n\n"
    NekoX += "**♡ My Master :** [LovelyPrince](https://t.me/BlackLover_Prince) "
    NekoX += f"Thanks For Adding Me In {yes.chat.title}"
    BUTTON = [
        [
            Button.url("【► Help ◄】", f"https://t.me/{BOT_USERNAME}?start=help"),
            Button.url("【► Support ◄】", f"https://t.me/{SUPPORT_CHAT}"),
        ]
    ]
    on = await neko.send_file(yes.chat_id, file=file2, caption=NekoX, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok = await neko.edit_message(yes.chat_id, on, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok2 = await neko.edit_message(yes.chat_id, ok, file=file4, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await neko.edit_message(yes.chat_id, ok2, file=file1, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok4 = await neko.edit_message(yes.chat_id, ok3, file=file2, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok5 = await neko.edit_message(yes.chat_id, ok4, file=file1, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok6 = await neko.edit_message(yes.chat_id, ok5, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok7 = await neko.edit_message(yes.chat_id, ok6, file=file4, buttons=BUTTON)
