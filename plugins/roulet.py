import plugins


def roulet(update, context):
    plugins.new_message.new_message(update)

    if plugins.enable_check.enable_check(__name__):
        return
    
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
    "🚀*Про розыгрыши:*"+
    "\n_Введи команду и получили шанс выиграть приз. У каждой команды свой приз и свои шансы._"+
    "\n*Испытай свою удачу прямо сейчас!*"+
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