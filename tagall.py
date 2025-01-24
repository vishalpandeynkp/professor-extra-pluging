import asyncio

from pyrogram import filters
from pyrogram.enums import ChatMembersFilter, ChatMemberStatus
from pyrogram.errors import FloodWait


SPAM_CHATS = []


@app.on_message(
    filters.command(
        ["all", "allmention", "mentionall", "tagall"] & filters.admin,
        prefixes=["/", "@"],
    )
)
async def tag_all_users(_, message):
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /cancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@all Hi Friends`"
        )
        return
    if replied:
        usernum = 0
        usertxt = ""
        try:
            SPAM_CHATS.append(message.chat.id)
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                name = f"{m.user.first_name} {m.user.last_name or ''}".strip()
                usertxt += f"[{name}](tg://user?id={m.user.id})  "
                if usernum == 7:
                    await replied.reply_text(
                        usertxt,
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""

            if usernum != 0:
                await replied.reply_text(
                    usertxt,
                    disable_web_page_preview=True,
                )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        try:
            usernum = 0
            usertxt = ""
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            async for m in app.get_chat_members(message.chat.id):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                name = f"{m.user.first_name} {m.user.last_name or ''}".strip()
                usertxt += f"[{name}](tg://user?id={m.user.id})  "
                if usernum == 7:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                await app.send_message(
                    message.chat.id,
                    f"{text}\n\n{usertxt}",
                    disable_web_page_preview=True,
                )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


async def tag_all_admins(_, message):
    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ɪs ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ sᴛᴏᴘ sᴏ ᴜsᴇ /cancel"
        )
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "** ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ ᴛᴀɢ ᴀʟʟ, ʟɪᴋᴇ »** `@admins Hi Friends`"
        )
        return
    if replied:
        usernum = 0
        usertxt = ""
        try:
            SPAM_CHATS.append(message.chat.id)
            async for m in app.get_chat_members(
                message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                name = f"{m.user.first_name} {m.user.last_name or ''}".strip()
                usertxt += f"[{name}](tg://user?id={m.user.id})  "
                if usernum == 7:
                    await replied.reply_text(
                        usertxt,
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(1)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                await replied.reply_text(
                    usertxt,
                    disable_web_page_preview=True,
                )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass
    else:
        usernum = 0
        usertxt = ""
        try:
            text = message.text.split(None, 1)[1]
            SPAM_CHATS.append(message.chat.id)
            async for m in app.get_chat_members(
                message.chat.id, filter=ChatMembersFilter.ADMINISTRATORS
            ):
                if message.chat.id not in SPAM_CHATS:
                    break
                if m.user.is_deleted or m.user.is_bot:
                    continue
                usernum += 1
                name = f"{m.user.first_name} {m.user.last_name or ''}".strip()
                usertxt += f"[{name}](tg://user?id={m.user.id})  "
                if usernum == 7:
                    await app.send_message(
                        message.chat.id,
                        f"{text}\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                    await asyncio.sleep(2)
                    usernum = 0
                    usertxt = ""
            if usernum != 0:
                await app.send_message(
                    message.chat.id,
                    f"{text}\n\n{usertxt}",
                    disable_web_page_preview=True,
                )
        except FloodWait as e:
            await asyncio.sleep(e.value)
        try:
            SPAM_CHATS.remove(message.chat.id)
        except Exception:
            pass


@app.on_message(
    filters.command(["admin", "admins", "report"], prefixes=["/", "@"]) & filters.group
)
async def admintag_with_reporting(client, message):
    if not message.from_user:
        return
    chat_id = message.chat.id
    from_user_id = message.from_user.id
    if message.chat.is_admin:
        return await tag_all_admins(client, message)

    if len(message.text.split()) <= 1 and not message.reply_to_message:
        return await message.reply_text("Reply to a message to report that user.")

    reply = message.reply_to_message or message
    reply_user_id = reply.from_user.id if reply.from_user else reply.sender_chat.id
    linked_chat = (await client.get_chat(chat_id)).linked_chat
    user = await app.get_chat_member(chat_id, reply_user_id)

    if reply_user_id == app.id:
        return await message.reply_text("Why would I report myself?")
    elif user.status == ChatMemberStatus.OWNER:
        return await message.reply("Do you know who is he/she, OWNER")
    elif (
        user.status == ChatMemberStatus.ADMINISTRATOR
        or reply_user_id == chat_id
        or (linked_chat and reply_user_id == linked_chat.id)
    ):
        return await message.reply_text(
            "Do you know that the user you are replying to is an admin?"
        )

    user_mention = reply.from_user.mention if reply.from_user else "the user"
    text = f"Reported {user_mention} to admins!."

    async for m in app.get_chat_members(
        chat_id, filter=ChatMembersFilter.ADMINISTRATORS
    ):
        if not m.user.is_bot and not m.user.is_deleted:
            text += f"[\u2063](tg://user?id={m.user.id})"

    await reply.reply_text(text)


@app.on_message(
    filters.command(
        [
            "stopmention",
            "cancel",
            "cancelmention",
            "offmention",
            "mentionoff",
            "cancelall",
        ]
        & filters.admin,
        prefixes=["/", "@"],
    )
)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("**ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss sᴜᴄᴄᴇssғᴜʟʟʏ sᴛᴏᴘᴘᴇᴅ!**")

    else:
        await message.reply_text("**ɴᴏ ᴘʀᴏᴄᴇss ᴏɴɢᴏɪɴɢ!**")
        return


__MODULE__ = "Tᴀɢᴀʟʟ"
__HELP__ = """

**@all or /all | /tagall or @tagall | /mentionall or @mentionall [text] or [reply to any message]** - To tag all users in your group using the bot.

**/admins | @admins | /report [text] or [reply to any message]** - To tag all admins in your group.

> If an admin uses this command, it will mention all admins in the group.

> If a regular user uses this command, it will be treated as a report and notify all admins.

**/cancel or @cancel | /offmention or @offmention | /mentionoff or @mentionoff | /cancelall or @cancelall** - To stop running any tag process.

"""
