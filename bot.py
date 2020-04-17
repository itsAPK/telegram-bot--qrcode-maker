import telebot
import pyqrcode
import time

token="<your_bot_token>"
bot=telebot.TeleBot(token)

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


while True:
	try:
		bot.infinity_polling(True)
	except Exception:
		time.sleep(1)
