from telegram.ext import Updater, CommandHandler

def main():
    #carpeta bot_token el key del bot, gestionar comunicacion a telegram
    updater = Updater(token=open("./bot_token").read(), use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start",start))#añadiendo un menejador de comando /start
    updater.dispatcher.add_handler(CommandHandler("repite",repite)) #añadiendo un menejador de comando /repite
    updater.dispatcher.add_handler(CommandHandler("suma",suma)) #añadiendo un menejador de comando /suma
    updater.start_polling() #preguntar todo el rato si hay notifacion nueva, funcionando bot
    updater.idle() #terminar bot 

def start(update, context):
    update.message.reply_text("Hola soy un bot geek")
    pass 

def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    # args[2,2]
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("El Resultado es: " + str(resultado))

main()