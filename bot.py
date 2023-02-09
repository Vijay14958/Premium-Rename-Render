import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6172299567:AAGTm2oQSi46HJB609EaUHzpFJMPWPNuVJA")

API_ID = int(os.environ.get("API_ID", "19134188"))

API_HASH = os.environ.get("API_HASH", "91587601a5d898e3341b7e4a9e1c2537")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
