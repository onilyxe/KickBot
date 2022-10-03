import plugins


def bluetext(update, context):
    plugins.new_message.new_message(update)

    if plugins.enable_check.enable_check(__name__):
        return
    
    context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
    "/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /ISS /ATTRACTED /TO /COLORS")