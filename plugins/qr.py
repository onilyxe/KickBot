from plugins import new_message, enable_check
from telegram import ChatAction


def qr(update, context):
    new_message.new_message(update)

    if enable_check.enable_check(__name__):
        return

    if not context.args:
        context.bot.send_message(chat_id=update.message.chat_id, parse_mode='markdown', text=
            '⚙️*QR*\n`/qr [text]`')
        return

    text = ' '.join(context.args)
    url = f"https://api.qrserver.com/v1/create-qr-code/?data={text}&amp;size=600x600"
    context.bot.send_chat_action(update.message.chat_id, ChatAction.UPLOAD_PHOTO)
    context.bot.send_photo(chat_id=update.message.chat_id, photo=url)
