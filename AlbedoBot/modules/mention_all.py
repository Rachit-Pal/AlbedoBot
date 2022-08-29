import asyncio

from telethon import events
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin, ChannelParticipantCreator

from AlbedoBot import tbot

spam_chats = []


@tbot.on(
    events.NewMessage(
        pattern="^/tagall|/call|/tall|/all|/mentionall|#all|@all|@mentionall|@tagall|@utag(.*)",
    )
)
async def all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("This command Can Be Use In Groups And Channels/n")

    is_admin = False
    try:
        partici_ = await tbot(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("Only admins can mention all!")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("Give me one argument!")
    if event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg is None:
            return await event.respond(
                "I Can't Mention Members For Older Messages! (messages which are sent before I'm added to group)"
            )
    else:
        return await event.respond(
            "Reply To a Message Or Give Me Some Text To Mention Others"
        )

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in tbot.iter_participants(chat_id):
        if chat_id not in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
        if usrnum == 10:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}\n\nMeet Me Here🙈 @Besties_XD ✨🥀"
                await tbot.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@tbot.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if event.chat_id not in spam_chats:
        return await event.respond("There Is No Proccess On Going")
    try:
        spam_chats.remove(event.chat_id)
    except:
        pass
    return await event.respond("Mentioning Are Stopped")


__mod_name__ = "Mention All"
