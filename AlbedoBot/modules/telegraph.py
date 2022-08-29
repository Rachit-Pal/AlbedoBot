import os
from datetime import datetime

from PIL import Image
from telegraph import Telegraph, exceptions, upload_file
from telethon import types

from AlbedoBot import tbot
from AlbedoBot.events import register

TMP_DOWNLOAD_DIRECTORY = "tg-File/"
babe = "AlbedoBot"
telegraph = Telegraph()
data = telegraph.create_account(short_name=babe)
auth_url = data["auth_url"]


@register(pattern="^/t(gm|gt) ?(.*)")
async def telegrap(event):
    optional_title = event.pattern_match.group(2)
    if event.reply_to_msg_id:
        datetime.now()
        reply_msg = await event.get_reply_message()
        input_str = event.pattern_match.group(1)
        if input_str == "gm":
            downloaded_file_name = await tbot.download_media(
                reply_msg, TMP_DOWNLOAD_DIRECTORY
            )
            datetime.now()
            if not downloaded_file_name:
                await tbot.send_message(event.chat_id, "Not Supported Format Media!")
                return
            if downloaded_file_name.endswith((".webp")):
                resize_image(downloaded_file_name)
            try:
                datetime.now()
                media_urls = upload_file(downloaded_file_name)
            except exceptions.TelegraphException as exc:
                await event.reply(f"ERROR: {str(exc)}")
                os.remove(downloaded_file_name)
            else:
                datetime.now()
                os.remove(downloaded_file_name)
                await tbot.send_message(
                    event.chat_id,
                    "Your telegraph is complete uploaded!",
                    buttons=[
                        [
                            types.KeyboardButtonUrl(
                                "➡ View Telegraph",
                                f"https://te.legra.ph{media_urls[0]}",
                            )
                        ]
                    ],
                )

        elif input_str == "gt":
            user_object = await tbot.get_entity(reply_msg.sender_id)
            title_of_page = user_object.first_name  # + " " + user_object.last_name
            # apparently, all Users do not have last_name field
            if optional_title:
                pass
            page_content = reply_msg.message
            if reply_msg.media:
                if page_content != "":
                    pass
                else:
                    await tbot.send_message(event.chat_id, "Not Supported Format Text!")
                downloaded_file_name = await tbot.download_media(
                    reply_msg, TMP_DOWNLOAD_DIRECTORY
                )
                m_list = None
                with open(downloaded_file_name, "rb") as fd:
                    m_list = fd.readlines()
                for m in m_list:
                    page_content += m.decode("UTF-8") + "\n"
                os.remove(downloaded_file_name)
            page_content = page_content.replace("\n", "<br>")
            datetime.now()
            await tbot.send_message(
                event.chat_id,
                "Your telegraph is complete uploaded!",
                buttons=[
                    [
                        types.KeyboardButtonUrl(
                            "➡ View Telegraph",
                            f"https://telegra.ph{media_urls[0]}",
                        )
                    ]
                ],
            )

    else:
        await event.reply("Reply to a message to get a permanent telegra.ph link.")


def resize_image(image):
    im = Image.open(image)
    im.save(image, "PNG")


__mod_name__ = "Telegraph"
