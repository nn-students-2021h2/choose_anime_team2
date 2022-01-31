import logging

from setup import PROXY, TOKEN
from telegram import Bot, Update
from telegram.ext import CallbackContext, CommandHandler, Filters, MessageHandler, Updater

from user_class import User
from anime_class import Anime

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.


def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text(f'Добрый день, {update.effective_user.first_name}!'
                              f'Я с радостью подберу для Вас аниме.')


def chat_help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Введи команду /start для начала. ')


def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning(f'Update {update} caused error {context.error}')


def take_users_info(update: Update, context: CallbackContext):
    """sex, age of a person"""
    pass


def take_anime_criteria(update: Update, context: CallbackContext):
    """setting and genre of preferable anime"""
    pass


def main():
    # bot = Bot(
    #     token=TOKEN,
    #     base_url=PROXY,  # delete it if connection via VPN
    # )
    # updater = Updater(bot=bot, use_context=True)

    # Connect via socks proxy
    REQUEST_KWARGS = {
        #'proxy_url': PROXY,  # Uncomment this line if you encounter network issues/timeouts when starting the bot
                              # Fill in the PROXY variable in setup.py with a proper proxy URL for this to work.

        # Optional, if you need authentication:
        # 'urllib3_proxy_kwargs': {
        #     'username': 'name',
        #     'password': 'passwd',
        # }
    }

    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS, use_context=True)

    # on different commands - answer in Telegram
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', chat_help))

    # on noncommand i.e message - echo the message on Telegram
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    updater.dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    logger.info('Start Bot')
    main()
