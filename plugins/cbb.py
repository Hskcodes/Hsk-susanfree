#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>╔════════════⦿\n├⋗ ᴄʀᴇᴀᴛᴏʀ : <a href='tg://user?id={831859341}'>zb network </a>\n├⋗ ʟᴀɴɢᴜᴀɢᴇ : <code>Python3</code>\n├⋗ ʟɪʙʀᴀʀʏ : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio 2.0.106</a>\n├⋗ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href=https://t.me/zblivebot>File Store Bot</a>\n├⋗ Main Channel : <a href=https://t.me/zbbackup>Zb Network</a>\n├⋗ Support Group : <a href=https://t.me/+NdifFX8P1pMwOGY0>Chat Weebs</a>\n╚═════════════════⦿</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
