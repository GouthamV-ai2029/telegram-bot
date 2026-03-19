import telebot
from flask import Flask, request
import os

TOKEN = "8748531687:AAG8cQiy95YB_lRMxp5AofzcMv6FxV1plxM"

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200

@app.route('/')
def home():
    return "Bot Running 🚀"

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hello from Render Webhook")

if __name__ == "__main__":
    PORT = int(os.environ.get('PORT', 10000))
    app.run(host="0.0.0.0", port=PORT)