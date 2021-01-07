from datetime import datetime
from typing import Optional, List
from telegram import Update, Bot
from telegram.ext import CommandHandler
from tg_bot import dispatcher
from zalgo_text import zalgo    

def zal(bot: Bot, update: Update, args):
    current_time = datetime.strftime(datetime.now(), "%d.%m.%Y %H:%M:%S")
    if update.message.reply_to_message is not None:
        args = update.message.reply_to_message.text
        args = args.split(" ")
    input_text = " ".join(args).lower()
    if input_text == "":
        update.message.reply_text("Type in some text!")
        return
    zalgofied_text = zalgo.zalgo().zalgofy(input_text)
    update.message.reply_text(zalgofied_text)

dispatcher.add_handler(CommandHandler('zal', zal, pass_args=True))
