import telebot
import json

BOT_TOKEN = "8726049487:AAFr-7C9nfXwfEQz1ymXwT3Fj_62oB5vIjI"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda m: True)
def handle_msg(message):
    
    data = {
        "user_id": message.chat.id,
        "text": message.text
    }

    with open("database.json", "a") as f:
        f.write(json.dumps(data) + "\n")

    bot.reply_to(message, "Message received")

bot.infinity_polling()