from pyrogram import filters
from config import Config
from utils.database import db

def admin_handlers(app):

    @app.on_message(filters.command("ban") & filters.user(Config.OWNER_ID))
    async def ban_user(client, message):
        if len(message.command) < 2:
            return await message.reply("❌ Provide user ID to ban.")
        uid = int(message.command[1])
        await db.ban_user(uid)
        await message.reply(f"🚫 Banned user `{uid}`")

    @app.on_message(filters.command("unban") & filters.user(Config.OWNER_ID))
    async def unban_user(client, message):
        if len(message.command) < 2:
            return await message.reply("❌ Provide user ID to unban.")
        uid = int(message.command[1])
        await db.unban_user(uid)
        await message.reply(f"✅ Unbanned user `{uid}`")

    @app.on_message(filters.command("banlist") & filters.user(Config.OWNER_ID))
    async def list_bans(client, message):
        bans = await db.get_ban_list()
        if bans:
            await message.reply("🚫 Banned Users:\n" + "\n".join(map(str, bans)))
        else:
            await message.reply("✅ No banned users.")

    @app.on_message(filters.command("broadcast") & filters.user(Config.OWNER_ID))
    async def broadcast_message(client, message):
        if len(message.command) < 2:
            return await message.reply("❌ Provide a message to broadcast.")
        text = message.text.split(None, 1)[1]
        users = await db.get_all_users()
        for uid in users:
            try:
                await app.send_message(uid, text)
            except:
                pass
        await message.reply("📢 Broadcast completed.")
