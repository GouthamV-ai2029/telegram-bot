import streamlit as st
import telebot
import threading

BOT_TOKEN = "8726049487:AAFr-7C9nfXwfEQz1ymXwT3Fj_62oB5vIjI"

bot = telebot.TeleBot(BOT_TOKEN)

if "messages" not in st.session_state:
    st.session_state.messages = []

@bot.message_handler(func=lambda m: True)
def handle_message(message):
    st.session_state.messages.append((message.chat.id, message.text))

def run_bot():
    bot.infinity_polling()

# Start bot only once
if "bot_started" not in st.session_state:
    thread = threading.Thread(target=run_bot)
    thread.daemon = True
    thread.start()
    st.session_state.bot_started = True

st.title("Telegram Bot Dashboard")

st.write("Received messages:")

for user, msg in st.session_state.messages:
    st.write(f"{user}: {msg}")