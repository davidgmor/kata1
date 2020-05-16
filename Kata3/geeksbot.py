from telegram.ext import Updater, CommandHandler
'''python-telegram-bot'''

def main():
    # Instanciamos updater
    updater = Updater(token=open('./bot_token').read(), use_context=True)

    # Añadimos un manejador al comando /start
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('repeat', repeat))
    updater.dispatcher.add_handler(CommandHandler('sum', sum))

    # Empezamos a pedir notificaciones a telegram
    updater.start_polling()

    # Capturamos señales de parada
    updater.idle()

def start(update, context):
    update.message.reply_text('Hola, soy un bot')
    pass

def repeat(update, context):
    update.message.reply_text(update.message.text)
    pass

def sum(update, context):
    result = int(context.args[0]) + int(context.args[1])
    update.message.reply_text(f'El resultado es {result}')
    pass

main()