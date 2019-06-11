#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import telegram
import os
from telegram.error import NetworkError, Unauthorized
from time import sleep
from emoji import emojize

update_id = None

# Definitions
TELEGRAM_USERNAME = [YOUR_TELEGRAM_USERNAME_HERE]
PC_USERNAME = [YOUR_PC_USERNAME_HERE]

def main():
    """Run the bot."""
    global update_id

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
    """Echo the message the user sent."""
    global update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:
            if update.message.from_user.username == TELEGRAM_USERNAME:  # Security check (Check if you are the sender)
                os.system("start firefox.exe " + update.message.text)
                update.message.reply_text(emojize(":white_check_mark:", use_aliases=True))
            else: # If you are not the sender, an intruder is detected, so the action is not run and its username and id are sent to a log file
                os.system("cd C:\\Users\\"+ YOUR_PC_USERNAME_HERE + "\\Desktop && echo Username: " + update.message.from_user.username + " ID: " + str(update.message.from_user.id) + " >> intruder.log")

if __name__ == '__main__':
    main()
