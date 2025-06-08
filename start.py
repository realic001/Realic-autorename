# handlers/start.py

from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start_handler(client: Client, message: Message):
    await message.reply_text(
        "👋 Hello! I'm zoro auto rename Bot!\n\n"
        "📁 I can rename files, set thumbnails, format filenames, and much more.\n"
        "Use the menu or send a file to get started!"
    )
