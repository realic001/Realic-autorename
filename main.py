import asyncio
from pyrogram import Client, idle
from config import Config
from handlers import register_all_handlers

app = Client(
    "FileRenameBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

async def main():
    await app.start()
    print("Bot started")
    register_all_handlers(app)
    if Config.WEB_SERVER:
        from web import start_webserver
        await start_webserver()
    await idle()
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
