from plugins import new_message, enable_check
from telegram.ext import Updater, CommandHandler


def start(update, context):
    new_message.new_message(update)

    if enable_check.enable_check(__name__):
        return
    
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
    "👋Привет. Я бот с небольшим набором функций, но с большим набором розыгрышей😏\n\nНапиши /help чтобы узнать что я умею.")
    
    
def help(update, context):
    
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
    "⚙️*Список команд:*"+
    "\n*/start* — _запустить бота._"+
    "\n*/help* — _это сообщение._"+
    "\n*/plugin* — _управление плагинами (Только для админа бота)._"+
    "\n*/id* — _твой id._"+
    "\n*/id g* — _id чата._"+
    "\n*/qr [text]* — _конвектор в qr code._"+
    "\n*/echo [text]* — _повторяет текст._"+
    "\n*/bluetext* — _синий текст._"+
    "\n\n🤭*И то, ради чего создавался бот.*"+
    "\n🥳*Розыгрыши:*"+
    "\n*/roulet* — _список розыгрышей._")
    
    
def nigger(update, context):
    
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
    "😂😂😂😂😂😂😂😂😂")