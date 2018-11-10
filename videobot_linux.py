import logging
import telegram
import os
from telegram.error import NetworkError, Unauthorized
from time import sleep
from emoji import emojize

update_id = None


def main():
    global update_id
    # Telegram Bot Authorization Token
    bot = telegram.Bot('YOUR_TOKEN_HERE')

    try:
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    while True:
        try:
            echo(bot)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            update_id += 1


def echo(bot):
    global update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:
            os.system("xdg-open " + update.message.text)
            update.message.reply_text(emojize(" :white_check_mark:", use_aliases=True))


if __name__ == '__main__':
    main()
