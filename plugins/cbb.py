#Coded by @Its_Tartaglia_Childe

from pyrogram import Client 
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text = f"<b>Bot Commands\n❏ Commands For BOT Admins\n├/start : start the bot or get posts\n├/batch : Create Group Message\n├/genlink : create link for one post\n├/users : view bot statistics\n├/broadcast : broadcast Message\n└/stats : checking your bot uptime\n\n👨‍💻 Developed by <a href=https://t.me/supernovanetwork>Supernova™</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗿 Close the page", callback_data="close"),
                        InlineKeyboardButton("🤔 About", callback_data="about")
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text = f"<b>\n⋉ Creator : <a href='tg://user?id={760067286}'>𝙓𝙚𝙣𝙤𝙫</a>\n❐ Owner : <a href='tg://user?id={OWNER_ID}'>This User\n❐ Support Group: <a href=https://t.me/sn_botsupport>Bots Support™</a>\n❐ Powered by: <a href=https://t.me/supernovanetwork>Supernova™</a>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━/n➮ Want your own Bot?: <a href=https://t.me/not_xenov>Contact here</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🗿 Close the page", callback_data="close"),
                        InlineKeyboardButton("🤔 About", callback_data="help")
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
