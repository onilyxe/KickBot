from plugins import new_message, enable_check
from telegram.ext import Updater, CommandHandler


def bluetext(update, context):
    new_message.new_message(update)

    if enable_check.enable_check(__name__):
        return
    
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
    "/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /ISS /ATTRACTED /TO /COLORS")
    
    
def blue(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def text(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def must(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def click(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def i(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def am(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def a(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def stupid(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def animal(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def that(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def iss(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def attracted(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def to(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')
    
    
def colors(update, context):

    context.bot.kick_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    context.bot.unban_chat_member(chat_id=update.message.chat_id, user_id=update.message.from_user['id'])
    update.message.reply_text(text=f'Потыкай')