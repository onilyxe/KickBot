from plugins import new_message, enable_check
from telegram.error import BadRequest
from telegram.ext import Updater, CommandHandler


def yapedarasik(update, context):
    new_message.new_message(update)

    if enable_check.enable_check(__name__):
        return

    try:
        context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
        context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
        update.message.reply_text(parse_mode='markdown', text=f'😢*К сожалению, ты не выиграл.*\n_Попробуй ещё раз_')

    except BadRequest:
        update.message.reply_text(parse_mode='markdown', text=f'😢*К сожалению, ты не выиграл.*\n_Попробуй ещё раз_')
