import urllib.request
from typing import Optional, List
from telegram import Update, Bot
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
import wikipedia

def wiki(bot: Bot, update: Update, args):
    reply = " ".join(args)
    summary = '{} <a href="{}">more</a>'
    update.message.reply_text(summary.format(wikipedia.summary(reply, sentences=3), wikipedia.page(reply).url))
		
__help__ = """
 - /wiki text: Returns search from wikipedia for the input text
"""
__mod_name__ = "WikiPedia"
WIKI_HANDLER = DisableAbleCommandHandler("wiki", wiki, pass_args=True)
dispatcher.add_handler(WIKI_HANDLER)
