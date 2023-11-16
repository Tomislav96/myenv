from telegram.ext import Updater, CommandHandler

def send_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I am your bot!")

def main():
    updater = Updater("6571829360:AAHDt_AJwBu2pAABBkSZUdoZVzUfn1PB1lw")
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("sendmessage", send_message))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()