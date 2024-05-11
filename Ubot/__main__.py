import importlib
import time
from datetime import datetime
import asyncio
from pyrogram import idle

from uvloop import install
from Ubot import aiosession, bots, app, ids, event_loop
from platform import python_version as py
from .logging import LOGGER
from pyrogram import __version__ as pyro
from Ubot.modules import ALL_MODULES
from Ubot.core.db import *
from Ubot.core import *
from ubotlibs import *
from config import SUPPORT, CHANNEL
import os
from dotenv import load_dotenv


BOT_VER ="8.1.0"


MSG_ON = """
**Dan Userbot Actived ✅**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
◉ **Versi** : `{}`
◉ **Phython** : `{}`
◉ **Pyrogram** : `{}`
**Ketik** `alive` **untuk Mengecheck Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""


async def main():
    await app.start()
    LOGGER("Dan Ubot").info("Memulai Ubot Pyro..")
    for all_module in ALL_MODULES:
        importlib.import_module("Ubot.modules" + all_module)
    for bot in bots:
        try:
            await bot.start()
            ex = await bot.get_me()
            user_id = ex.id
            await ajg(bot)
            await buat_log(bot)
            botlog_chat_id = await get_botlog(user_id)
            try:
                await bot.send_message(botlog_chat_id, MSG_ON.format(BOT_VER, py(), pyro))
            except BaseException as a:
                LOGGER("Info").warning(f"{a}")
            LOGGER("Info").info("Startup Completed")
            LOGGER("✓").info(f"Started as {ex.first_name} | {ex.id} ")
            ids.append(ex.id)
        except Exception as e:
            LOGGER("X").info(f"{e}")
            
    await idle()
    await aiosession.close()
    await app.stop()
    


if __name__ == "__main__":
    LOGGER("Dan Ubot").info("Starting  Ubot")
    install()
    event_loop.run_until_complete(main())

