import streamlit as st
import telebot
import threading

BOT_TOKEN = "8726049487:AAFr-7C9nfXwfEQz1ymXwT3Fj_62oB5vIjI"

bot = telebot.TeleBot(BOT_TOKEN)

messages = []

# Telegram bot handler
@bot.message_handler(func=lambda m: True)
def handle_msg(message):
    messages.append((message.chat.id, message.text))

# Run bot in background
def run_bot():
    bot.infinity_polling()

threading.Thread(target=run_bot, daemon=True).start()

# Streamlit UI
st.title("Telegram Bot Dashboard")

st.write("Messages received:")

for user, msg in messages:
    st.write(f"{user}: {msg}")t")