import plugins


def help(update, context):
    plugins.new_message.new_message(update)

    if plugins.enable_check.enable_check(__name__):
        return
    
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
    "⚙️*Список команд:*"+
    "\n*/start* — _запустить бота._"+
    "\n*/help* — _это сообщение._"+
    "\n*/id* — _твой id._"+
    "\n*/id g* — _id чата._"+
    "\n*/qr [text]* — _конвектор в qr code._"+
    "\n*/echo [text]* — _повторяет текст._"+
    "\n*/bluetext* — _синий текст._"+
    "\n\n🤭*И то, ради чего создавался бот.*"+
    "\n🥳*Розыгрыши:*"+
    "\n*/roulet* — _список розыгрышей._")