import asyncio
import os
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
os.system("pip install Extre")
from Extre import *
from Extre.utils import admin_cmd, sudo_cmd, load_module, humanbytes, register, command, start_assistant, errors_handler, progress, human_to_bytes, time_formatter, is_admin, amanpandey_cmd, extremepro_cmd
from Extre.config import Config
from Extre.variables import Var
from Extre import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from pathlib import Path
import asyncio
import telethon.utils



                    
async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("userbot starting telethon")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
    else:
        bot.start()
import glob
path = 'assistant/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        start_assistant(shortname.replace(".py", ""))   



import glob

path = 'plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))



print("userbot deployed WITH SUCESS ")



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()