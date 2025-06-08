from .rename import rename_handlers
from .caption import caption_handlers
from .thumb import thumb_handlers
from .queue import queue_handlers
from .admin import admin_handlers
from .start import start_handlers  # ✅ Add this

def register_all_handlers(app):
    rename_handlers(app)
    caption_handlers(app)
    thumb_handlers(app)
    queue_handlers(app)
    admin_handlers(app)
    start_handlers(app)  # ✅ Register start handler here
