from telegram.ext import Updater, CommandHandler
import yaml
import logging
from plugins import *


def start_bot():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logging.getLogger('apscheduler.executors.default').propagate = False

    with open('config.yaml', 'r') as f:
        config = yaml.full_load(f)

    api_key = config['TELEGRAM']['API_KEY']

    updater = Updater(token=api_key, use_context=True)
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('echo', echo.echo))
    dispatcher.add_handler(CommandHandler('id', id.id))
    dispatcher.add_handler(CommandHandler('qr', qr.qr))
    dispatcher.add_handler(CommandHandler('plugin', plugin.plugin))
    
    dispatcher.add_handler(CommandHandler('start', text.start))
    dispatcher.add_handler(CommandHandler('help', text.help))
    dispatcher.add_handler(CommandHandler('nigger', text.nigger))
    
    dispatcher.add_handler(CommandHandler('roulet', roulet.roulet))
    dispatcher.add_handler(CommandHandler('kekmi', roulet.kekmi))
    dispatcher.add_handler(CommandHandler('yadebil', roulet.yadebil))
    dispatcher.add_handler(CommandHandler('yagandone', roulet.yagandone))
    dispatcher.add_handler(CommandHandler('yapedarasik', roulet.yapedarasik))
    
    
    dispatcher.add_handler(CommandHandler('bluetext', bluetext.bluetext))
    dispatcher.add_handler(CommandHandler('a', bluetext.a))
    dispatcher.add_handler(CommandHandler('am', bluetext.am))
    dispatcher.add_handler(CommandHandler('animal', bluetext.animal))
    dispatcher.add_handler(CommandHandler('attracted', bluetext.attracted))
    dispatcher.add_handler(CommandHandler('blue', bluetext.blue))
    dispatcher.add_handler(CommandHandler('click', bluetext.click))
    dispatcher.add_handler(CommandHandler('colors', bluetext.colors))
    dispatcher.add_handler(CommandHandler('i', bluetext.i))
    dispatcher.add_handler(CommandHandler('iss', bluetext.iss))
    dispatcher.add_handler(CommandHandler('must', bluetext.must))
    dispatcher.add_handler(CommandHandler('stupid', bluetext.stupid))
    dispatcher.add_handler(CommandHandler('text', bluetext.text))
    dispatcher.add_handler(CommandHandler('that', bluetext.that))
    dispatcher.add_handler(CommandHandler('to', bluetext.to))
    

    updater.start_polling(drop_pending_updates=True)
    updater.idle()

if __name__ == '__main__':
    start_bot()