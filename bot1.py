import telebot
TOKEN = "8748531687:AAG8cQiy95YB_lRMxp5AofzcMv6FxV1plxM"
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    user_name = message.from_user
    text = f"Welcome {user_name} to the NVault"
    bot.send_message(message.chat.id,text)
bot.polling()