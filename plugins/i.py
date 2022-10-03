from plugins import new_message, enable_check
from telegram.ext import Updater, CommandHandler


def i(update, context):
    new_message.new_message(update)

    if enable_check.enable_check(__name__):
        return

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')