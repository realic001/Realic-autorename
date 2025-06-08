from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

client = AsyncIOMotorClient(Config.MONGO_URI)
db_conn = client.filebot

class db:

    @staticmethod
    async def set_caption(user_id, caption):
        await db_conn.captions.update_one({"_id": user_id}, {"$set": {"caption": caption}}, upsert=True)

    @staticmethod
    async def get_caption(user_id):
        data = await db_conn.captions.find_one({"_id": user_id})
        return data["caption"] if data else None

    @staticmethod
    async def delete_caption(user_id):
        await db_conn.captions.delete_one({"_id": user_id})

    @staticmethod
    async def ban_user(user_id):
        await db_conn.banned.update_one({"_id": user_id}, {"$set": {}}, upsert=True)

    @staticmethod
    async def unban_user(user_id):
        await db_conn.banned.delete_one({"_id": user_id})

    @staticmethod
    async def get_ban_list():
        cursor = db_conn.banned.find({})
        return [doc["_id"] async for doc in cursor]

    @staticmethod
    async def set_dump_channel(channel_id):
        await db_conn.settings.update_one({"_id": "dump_channel"}, {"$set": {"channel_id": channel_id}}, upsert=True)

    @staticmethod
    async def get_dump_channel():
        data = await db_conn.settings.find_one({"_id": "dump_channel"})
        return data["channel_id"] if data else None

    @staticmethod
    async def get_all_users():
        cursor = db_conn.users.find({})
        return [doc["_id"] async for doc in cursor]
