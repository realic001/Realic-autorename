import os

class Config:
    API_ID = int(os.getenv("API_ID", "123456"))
    API_HASH = os.getenv("API_HASH", "your_api_hash")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://user:pass@cluster.mongodb.net")
    OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))
    WEB_SERVER = os.getenv("WEB_SERVER", "True").lower() == "true"
    PORT = int(os.getenv("PORT", 8080))
    DOMAIN = os.getenv("DOMAIN", "0.0.0.0")
    DUMP_CHANNEL = int(os.getenv("DUMP_CHANNEL", "-1001234567890"))
    ADMINS = list(map(int, os.getenv("ADMINS", "123456789").split()))
