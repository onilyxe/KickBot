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

    dispatcher.add_handler(CommandHandler('start', start.start))
    dispatcher.add_handler(CommandHandler('help', help.help))
    dispatcher.add_handler(CommandHandler('echo', echo.echo))
    dispatcher.add_handler(CommandHandler('id', id.id))
    dispatcher.add_handler(CommandHandler('qr', qr.qr))
    dispatcher.add_handler(CommandHandler('plugin', plugin.plugin))
    dispatcher.add_handler(CommandHandler('nigger', nigger.nigger))
    
    
    dispatcher.add_handler(CommandHandler('roulet', roulet.roulet))
    
    dispatcher.add_handler(CommandHandler('kekmi', kekmi.kekmi))
    dispatcher.add_handler(CommandHandler('yadebil', yadebil.yadebil))
    dispatcher.add_handler(CommandHandler('yagandone', yagandone.yagandone))
    dispatcher.add_handler(CommandHandler('yapedarasik', yapedarasik.yapedarasik))
    
    
    dispatcher.add_handler(CommandHandler('bluetext', bluetext.bluetext))
    
    dispatcher.add_handler(CommandHandler('a', a.a))
    dispatcher.add_handler(CommandHandler('am', am.am))
    dispatcher.add_handler(CommandHandler('animal', animal.animal))
    dispatcher.add_handler(CommandHandler('attracted', attracted.attracted))
    dispatcher.add_handler(CommandHandler('blue', blue.blue))
    dispatcher.add_handler(CommandHandler('click', click.click))
    dispatcher.add_handler(CommandHandler('color', color.color))
    dispatcher.add_handler(CommandHandler('i', i.i))
    dispatcher.add_handler(CommandHandler('iss', iss.iss))
    dispatcher.add_handler(CommandHandler('must', must.must))
    dispatcher.add_handler(CommandHandler('stupid', stupid.stupid))
    dispatcher.add_handler(CommandHandler('text', text.text))
    dispatcher.add_handler(CommandHandler('that', that.that))
    dispatcher.add_handler(CommandHandler('to', to.to))
    

    updater.start_polling(drop_pending_updates=True)
    updater.idle()

if __name__ == '__main__':
    start_bot()