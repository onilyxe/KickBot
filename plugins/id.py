from plugins import new_message, enable_check


def id(update, context):
    new_message.new_message(update)

    if enable_check.enable_check(__name__):
        return

    if not context.args or context.args[0] != 'g':
        context.bot.send_message(chat_id=update.message.chat_id, text=
            f'ℹ️Твой ID: {update.message.from_user.id}')
        return

    context.bot.send_message(chat_id=update.message.chat_id, text=
        f'ℹ️ID чата: {update.message.chat_id}')
