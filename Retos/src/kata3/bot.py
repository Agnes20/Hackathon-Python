import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    update.message.reply_text("Hola, Geeks!")


def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""
    update.message.reply_text("Ayudenme!")

def mayus(update, context):
    resultado = str(context.args[0])
    resultado = resultado.upper()
    update.message.reply_text(resultado)

def alreves(update, context):
    """Repite el mensaje del usuario."""
    resultado = update.message.text
    for i in range(len(resultado),0,-1):
        resultado += i-1
    update.message.reply_text(resultado)

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater(token=open("./bot_token").read(), use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    updater.dispatcher.add_handler(CommandHandler("start",start))#añadiendo un menejador de comando /start
    updater.dispatcher.add_handler(CommandHandler("help",help)) #añadiendo un menejador de comando /help
    updater.dispatcher.add_handler(CommandHandler("mayus",mayus)) #añadiendo un menejador de comando /mayuscula
    updater.dispatcher.add_handler(CommandHandler("alreves",alreves)) #añadiendo un menejador de comando /alreves

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    
    lista = [start,help,mayus]


    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    #
    
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
