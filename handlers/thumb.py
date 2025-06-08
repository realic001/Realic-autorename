import os
from pyrogram import filters

THUMB_DIR = "downloads/thumbs"
os.makedirs(THUMB_DIR, exist_ok=True)

def thumb_handlers(app):

    @app.on_message(filters.command("sthum") & filters.photo)
    async def save_thumb(client, message):
        path = f"{THUMB_DIR}/{message.from_user.id}.jpg"
        await message.download(file_name=path)
        await message.reply("✅ Thumbnail saved.")

    @app.on_message(filters.command("viewthumb") & filters.private)
    async def view_thumb(client, message):
        path = f"{THUMB_DIR}/{message.from_user.id}.jpg"
        if os.path.exists(path):
            await message.reply_photo(path)
        else:
            await message.reply("❌ No thumbnail found.")

    @app.on_message(filters.command("delthumb") & filters.private)
    async def delete_thumb(client, message):
        path = f"{THUMB_DIR}/{message.from_user.id}.jpg"
        if os.path.exists(path):
            os.remove(path)
            await message.reply("🗑️ Thumbnail deleted.")
        else:
            await message.reply("❌ No thumbnail to delete.")
