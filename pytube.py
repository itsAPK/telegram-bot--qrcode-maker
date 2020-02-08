import pyqrcode
import telebot
import os
from flask import Flask, request

TOKEN = '837657264:AAHiwwz2YhJg_TZ4wEwN27ENw7rDgTxU_TA'
bot = telebot.TeleBot(TOKEN)
sever = Flask(__name__)


@bot.message_handler(commands=['strat'])
def send_Welcome(message):
    bot.reply_to(message, 'Welcome to QRCODE GENERATOR '
                          'Use /create to generate QRCODE')


@bot.message_handler(commands=['create'])
def qrcode_maker(message):
    url = pyqrcode.create(input('SEND THE LINK'))
    url.png('qrcode.png', scale=2)
    print(url.terminal(quiet_zone=1))


@sever.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates(telebot.types.Update.de_json(requests.stream.read().decode("utf-8")))
    return "!", 200


@sever.route('/')
def webhook():
    bot.set_webhook(url='' + TOKEN)
    return "!", 200


if __name__ == "__main":
    sever.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
