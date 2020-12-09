import requests
import os
 
from telegram import Update, Bot, ParseMode
from telegram.ext import run_async
 
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
 
@run_async
def ddlc(bot: Bot, update: Update):
    msg = update.effective_message
    args = update.effective_message.text.split(" ", 5)
    character = args[1]
    background = args[2]
    body = args[3]
    face = args[4]
    text = args[5]
    rq = requests.get(f"https://nekobot.xyz/api/imagegen?type=ddlc&character={character}&background={background}&body={body}&face={face}&text={text}").json()
    message = rq.get("message")
    # do shit with url if you want to
    if not message:
        msg.reply_text("No URL was received from the API!")
        return
    msg.reply_photo(message)
 
 
__help__ = """Characters - monika, yuri, natsuki, sayori or m, y, n , s

Background - bedroom, class, closet, club, corridor, house, kitchen, residential, sayori_bedroom

Body - there is only 1 or 2 for monika and 1, 1b, 2, 2b for the rest

Face - Every Alphabet Letter, For Yuri - y1, y2, y3, y4, y5, y6, y7

Text - BOTTOM TEXT

Usage: /ddlc <character> <background> <body> <face> <text>"""
__mod_name__ = "Neko"
 
DDLC_HANDLER = DisableAbleCommandHandler("Neko", Neko)
 
dispatcher.add_handler(DDLC_HANDLER)
 
 
