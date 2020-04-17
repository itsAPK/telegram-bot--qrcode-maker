import telebot
import pyqrcode
from flask import Flask,request
import time
import os


token="1166305238:AAGOk3BNVGUlMHaZqMVRlPZa5gOxazX4clg"
bot=telebot.TeleBot(token)

'''server=Flask(__name__)'''

@bot.message_handler(commands=['start'])
def start_message(msg):
    bot.send_chat_action(msg.chat.id, 'typing')
    bot.send_message(msg.chat.id,'Hey There,\n Use /qr_code to generate QR CODE ')

@bot.message_handler(commands=['qr_code'])
def qr_code_handler(message):    
    bot.send_chat_action(message.chat.id, 'typing')
    sent = bot.send_message(message.chat.id, "Send Text or Url")
    bot.register_next_step_handler(sent, qrcode)

def qrcode(message):
    url=pyqrcode.create(message.text)
    url.png('qrcode.png',scale=15)
    bot.send_chat_action(message.chat.id, 'upload_document')
    bot.send_document(message.chat.id,open('qrcode.png','rb' ))

'''@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200'''


'''@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='http://966fcf05.ngrok.io' + token)
    return "!", 200'''


'''if __name__ == "__main__":
    server.run(host="localhost", port=8000,debug=True)'''

while True:
	try:
		bot.infinity_polling(True)
	except Exception:
		time.sleep(1)