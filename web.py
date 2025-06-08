import asyncio
from aiohttp import web

async def start_webserver():
    async def index(request):
        return web.Response(text="Bot is alive", content_type="text/plain")

    app = web.Application()
    app.router.add_get("/", index)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", 8080)
    await site.start()
