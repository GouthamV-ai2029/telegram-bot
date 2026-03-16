import streamlit as st
import json

st.title("Telegram Dashboard")

try:
    with open("database.json") as f:
        lines = f.readlines()

    for line in lines:
        msg = json.loads(line)
        st.write(f"User: {msg['user_id']}")
        st.write(f"Message: {msg['text']}")
        st.divider()

except:
    st.write("No messages yet")