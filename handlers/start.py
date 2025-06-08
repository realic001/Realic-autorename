
from pyrogram import Client, filters
from pyrogram.types import Message

def start_handlers(app: Client):
    @app.on_message(filters.command("start"))
    async def start_handler(client: Client, message: Message):
        await message.reply_text(
            "👋 Hello! I'm Zoro Auto Rename Bot!\n\n"
            "📁 I can rename files, set thumbnails, format filenames, and much more.\n"
            "Use the menu or send a file to get started!"
        )
