from plugins import new_message, enable_check
from telegram.error import BadRequest
from telegram.ext import Updater, CommandHandler


def kekmi(update, context):
    new_message.new_message(update)

    if enable_check.enable_check(__name__):
        return

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    
    
def yagandone(update, context):

    try:
        context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
        context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
        update.message.reply_text(parse_mode='markdown', text=f'😢*К сожалению, ты не выиграл.*\n_Попробуй ещё раз_')

    except BadRequest:
        update.message.reply_text(parse_mode='markdown', text=f'🚀*Ты уже получил этот приз!*')


def yadebil(update, context):

    try:
        context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
        context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
        update.message.reply_text(parse_mode='markdown', text=f'😢*К сожалению, ты не выиграл.*\n_Попробуй ещё раз_')

    except BadRequest:
        update.message.reply_text(parse_mode='markdown', text=f'🚀*Ты уже получил этот приз!*')


def yapedarasik(update, context):

    try:
        context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
        context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
        update.message.reply_text(parse_mode='markdown', text=f'😢*К сожалению, ты не выиграл.*\n_Попробуй ещё раз_')

    except BadRequest:
        update.message.reply_text(parse_mode='markdown', text=f'😢*К сожалению, ты не выиграл.*\n_Попробуй ещё раз_')


def roulet(update, context):
    
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
    "🚀*Про розыгрыши:*"+
    "\n_Введи команду и получили шанс выиграть приз. У каждой команды свой приз и свои шансы. Не забудь добавить меня в групповой чат (розыгрыши работают только там) и выдать права администратора, иначе я не смогу работать😢_"+
    "\n\n🥳️*Список розыгрышей:*"+
    "\n*/yadebil*"+
    "\n*Приз:* _возможность закреплять сообщения._"+
    "\n*Шанс:* _10%_"+
    "\n*/yagandone*"+
    "\n*Приз:* _возможность получить администратора._"+
    "\n*Шанс:* _5%_"+
    "\n*/yapedarasik*"+
    "\n*Приз:* _возможность получить создателя._"+
    "\n*Шанс:* _1%_")