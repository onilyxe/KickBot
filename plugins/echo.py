from plugins import new_message, enable_check


def echo(update, context):
    new_message.new_message(update)

    if enable_check.enable_check(__name__):
        return

    if not context.args:
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
        '️ℹ️Нет аргумента.\n`/echo [text]`')
    else:
        all_words = ' '.join(context.args)
        context.bot.send_message(chat_id=update.message.chat_id, text=all_words)
