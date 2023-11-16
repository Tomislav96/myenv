import os
import random
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.error import Unauthorized  # Import Unauthorized exception

TOKEN = '6938900577:AAG0W4t54p9X2RLeZNrr6imZ-damCXifr34'
CHAT_ID = '-1002130321556'  # Replace with your channel username or ID
API_KEY = 'CW+zDauy5hYDe9rq17vjWg==l7s4vvujguepE8d9'

def get_quote():
    category = 'success'
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
    
    if response.status_code == requests.codes.ok:
        data = response.json()
        if data and len(data) > 0 and 'quote' in data[0] and 'author' in data[0]:
            return data[0]['quote'] + ' - ' + data[0]['author']
        else:
            print(f"Unexpected response format: {data}")
            return "No quotes available in the specified category."
    else:
        print(f"Error fetching quote. Status code: {response.status_code}, Response: {response.text}")
        return "Error fetching quote"

def send_quote(context: CallbackContext):
    try:
        quote = get_quote()
        print(f"Sending quote to {CHAT_ID}: {quote}")
        context.bot.send_message(chat_id=CHAT_ID, text=quote)
    except Unauthorized as e:
        print(f"Unauthorized error: {e}")
        print("Make sure the bot is a member of the channel and has the necessary permissions.")
    except Exception as e:
        print(f"Error sending quote to group: {e}")

def help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text("Everytime you relapse, you are that much weaker. Look beyond yourself and see the World outside!")

def start(update: Update, context: CallbackContext):
    update.message.reply_text('I will send you an inspirational quote every hour!')

def main():
    updater = Updater(TOKEN, use_context=True)
    job_queue = updater.job_queue

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help)) 

    # Schedule the job to send a random quote every hour
    job_queue.run_repeating(send_quote, interval=7200, first=0)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
