from pyrogram import (
    Client,
    filters
)
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from vars import var


START_MSG = """
Hi, I am **Saviour Coders' ANONYMOUS SENDER BOT.**\n
Just Forward me the messages or
media you want to save or remove forward tag and I will **Anonymize** that !!

"""

if var.START_MESSAGE is not None:
    START = var.START_MESSAGE
else:
    START = START_MSG


REPLY_MARKUP = InlineKeyboardMarkup([
    [InlineKeyboardButton("🐠 Support Group 🐠",
                          url="t.me/ubuntu_coders")],
    [InlineKeyboardButton("🦧 Support Channel 🦧",
                          url="t.me/UC_bot_channel")]
    [InlineKeyboardButton("🐬 Dev 🐬",
                          url="t.me/saviour_coder")]])


@Client.on_message(filters.command('start') & filters.private)
async def start(client, message):
    await message.reply_text(START,
                             reply_markup=REPLY_MARKUP)
