from pyrogram import filters
from config import Config
from utils.database import db

def queue_handlers(app):

    @app.on_message(filters.command("setdump") & filters.user(Config.OWNER_ID))
    async def set_dump(client, message):
        if len(message.command) < 2:
            return await message.reply("❌ Provide a channel ID (e.g. -1001234567890).")
        channel_id = int(message.command[1])
        await db.set_dump_channel(channel_id)
        await message.reply("✅ Dump channel set.")

    @app.on_message(filters.command("chkdump") & filters.user(Config.OWNER_ID))
    async def check_dump(client, message):
        cid = await db.get_dump_channel()
        await message.reply(f"📥 Dump Channel: `{cid}`")

    @app.on_message(filters.command("deldump") & filters.user(Config.OWNER_ID))
    async def del_dump(client, message):
        await db.set_dump_channel(None)
        await message.reply("🗑️ Dump channel deleted.")
