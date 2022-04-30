from telegram import KeyboardButton, ReplyKeyboardMarkup, Update
from telegram.ext import *
from utils import *

import tokens


@log_message
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to WordleBot! v0")


def main():
    updater = Updater(token=tokens.token)
    updater.dispatcher.add_handler(CommandHandler(command='start', callback=start))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
