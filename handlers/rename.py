from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

def rename_handlers(app):

    @app.on_message(filters.private & (filters.document | filters.video | filters.audio))
    async def file_receive(client, message):
        file = message.document or message.video or message.audio
        filename = file.file_name
        filesize = file.file_size
        await message.reply_text(
            f"**File Received:** `{filename}`\n**Size:** `{filesize / 1024 / 1024:.2f} MB`",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Rename", callback_data="rename")]]
            ),
        )

    @app.on_callback_query(filters.regex("rename"))
    async def ask_new_name(client, callback_query):
        await callback_query.message.edit("Send me the new filename (with extension):")
        if not hasattr(app, "user_data"):
            app.user_data = {}
        app.user_data[callback_query.from_user.id] = {
            "rename": True,
            "file_msg": callback_query.message.reply_to_message
        }

    @app.on_message(filters.private & filters.text)
    async def handle_new_filename(client, message):
        if not hasattr(app, "user_data"):
            app.user_data = {}
        data = app.user_data.get(message.from_user.id)
        if data and data.get("rename"):
            original_msg = data["file_msg"]
            file = original_msg.document or original_msg.video or original_msg.audio
            new_name = message.text.strip()
            downloaded = await original_msg.download(file_name=new_name)
            await message.reply_document(downloaded, caption=f"Renamed to: `{new_name}`")
            os.remove(downloaded)
            del app.user_data[message.from_user.id]
