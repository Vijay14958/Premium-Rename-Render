import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','6172299567:AAGTm2oQSi46HJB609EaUHzpFJMPWPNuVJA')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"Total User:- {total_user()}\nBot :- @filerenamevjbot\nCreater :- @Anjel_Neha\nLanguage :-Python3\nLibrary :- Pyrogram\nServer :- Oracle Cloud\nTotal Renamed File :-{total_rename}\nTotal Size Renamed :- {humanbytes(int(total_size))} ",quote=True)
