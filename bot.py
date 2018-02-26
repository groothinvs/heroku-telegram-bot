#!/usr/bin/env python3
from telegram.ext import Updater, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

def welcome(bot: Bot, update: Update):
    msg = update.effective_message
    chat = update.effective_chat
    usr = update.effective_user

    for u in msg.new_chat_members:
        bot.sendMessage(chat.id, 'Welcome {} to {}! Please read the pinned message.'.format(u.mention_html(), chat.title), parse_mode='HTML')


if __name__ == "__main__":
    ud = Updater(token='546028656:AAGOJ93532CE_w_IM6jrdw2EurWqMOB7A58')
    dp = ud.dispatcher

    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))

    ud.start_polling()
    ud.idle()
