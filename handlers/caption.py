from pyrogram import filters

from utils.database import db

def caption_handlers(app):

    @app.on_message(filters.command("setcp") & filters.private)
    async def set_caption(client, message):
        if len(message.command) < 2:
            return await message.reply("❌ Please provide a caption text.")
        caption = message.text.split(None, 1)[1]
        await db.set_caption(message.from_user.id, caption)
        await message.reply("✅ Caption set successfully.")

    @app.on_message(filters.command("chckcp") & filters.private)
    async def check_caption(client, message):
        caption = await db.get_caption(message.from_user.id)
        await message.reply(caption or "❌ No caption set.")

    @app.on_message(filters.command("delcp") & filters.private)
    async def delete_caption(client, message):
        await db.delete_caption(message.from_user.id)
        await message.reply("🗑️ Caption deleted.")
