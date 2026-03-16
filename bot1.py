import telebot

from telebot import types
import qrcode
from io import BytesIO
import random
BOT_TOKEN = "8598180553:AAF9m0dCrasDzO9y31JPwXkdZHuiHMttS9U"
ADMIN_ID = {7745765588,8695947788}
ADMIN_USERNAME = "GOOD_BOY_BANNY1433"
UPI_ID = "banny143@ptyes"
PAYEE_NAME = "Telegram Sessions"
BOT_USERNAME = "OTP_SELLING_3_BOT"
CHANNEL_ID = -1003555274207
CHANNEL_USERNAME = "otp_bot_support143" 
LAST_USER_ID =None
SUPPORT_TEXT = (
    "🆘 <b>Premium Support</b>\n\n"
    "Need help? Contact admin 👇\n\n"
    f"👨‍💼 <b>Admin:</b> @{ADMIN_USERNAME}\n"
    f"🆔 <b>Admin IDs:</b> <code>{', '.join(map(str, ADMIN_ID))}</code>\n\n"
    "💳 Payment • 📱 Number • 💰 Referral\n"
   
)

USER_COUNTRY = {}
user_state = {}
ALL_USERS = set()

bot = telebot.TeleBot(BOT_TOKEN)
def send_premium_otp(chat_id, otp, password):
    msg = f"""
🔐 <b>YOUR OTP: {otp}</b>
🔑 <b>YOUR PASSWORD:</b> <code>{password}</code>

✅ Please use this OTP and PASSWORD to login to your Telegram.

🚫 Do NOT share this information with anyone.
✨ Powered by Telegram Sessions

✅ Thank you for purchasing.
"""
    bot.send_message(chat_id, msg, parse_mode="HTML")
def show_stock(chat_id):
    text = "📦 <b>Available Stock</b>\n\n"

    for code, data in COUNTRIES.items():
        count = len(COUNTRY_NUMBERS.get(code, []))

        if count > 0:
            text += f"{data['NAME']} → ✅ <b>{count}</b> available\n"
        else:
            text += f"{data['NAME']} → ❌ Out of stock\n"

    bot.send_message(chat_id, text, parse_mode="HTML")
def safe_send_photo(chat_id, photo, caption=None,reply_markup=None):
    try:
    		bot.send_photo(chat_id,photo,caption=caption,reply_markup=reply_markup)
    except Exception as e:
        print(f"Failed to send photo to {chat_id}:{e}")
        
def force_join(chat_id):
    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton("🔔 join channel", url=f"https://t.me/{CHANNEL_USERNAME}"))
    kb.add(types.InlineKeyboardButton("✅ Joined", callback_data="home"))
    
    bot.send_message(
    	chat_id, 
		"🚫 <b>You must join our channel to use this bot</b>",
        reply_markup= kb,
        parse_mode="HTML")
def is_user_joined(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ["member", "administrator", "creator"]
    except:
        return False
        
COUNTRIES = {
    "india": {"NAME": "🇮🇳 INDIA", "PRICE": 35, "STOCK": True},
    "usa": {"NAME": "🇺🇸 USA", "PRICE": 60, "STOCK": True},
    "zimbabwe": {"NAME": "🇿🇼 ZIMBABWE", "PRICE": 40, "STOCK": True},
    "bangladesh": {"NAME": "🇧🇩 BANGLADESH", "PRICE": 40, "STOCK": True},
    "ethiopia": {"NAME": "🇪🇹 ETHIOPIA", "PRICE": 60,"STOCK": True},
    "iran":{"NAME": "🇮🇷 IRAN", "PRICE":55, "STOCK": True},
    "myanmar": {"NAME": "🇲🇲 MYANMAR","PRICE":37,"STOCK":True}
}
COUNTRY_NUMBERS = {
	"iran": [],
    "usa": [],
    "india":[],
    "bangladesh":[],
    "ethiopia":[],
    "nepal": [],
    "myanmar":[]
}

def send_payment_qr(chat_id, amount):
    upi_url = f"upi://pay?pa={UPI_ID}&pn={PAYEE_NAME}&am={amount}&cu=INR"

    qr = qrcode.make(upi_url)
    bio = BytesIO()
    bio.name = "payment.png"
    qr.save(bio, "PNG")
    bio.seek(0)

    bot.send_photo(
        chat_id,
        bio,
        caption=(
            f"📷 <b>Scan & Pay</b>\n\n"
            f"💰 Amount: ₹{amount}\n\n"
            "📌 Send payment screenshot after paying"
        ),
        parse_mode="HTML"
    )
    


def send_upi_qr(chat_id, amount):
    upi_id = "banny143@ptyes"
    name = "Telegram Sessions"

    upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

    qr = qrcode.make(upi_link)
    qr.save("upi_qr.png")

    with open("upi_qr.png", "rb") as photo:
        bot.send_photo(
            chat_id,
            photo,
            caption=f"💰 Amount: ₹{amount}\n\nAfter payment, send your UTR number."
        )
def main_menu(chat_id, message_id=None):
    kb = types.InlineKeyboardMarkup(row_width=2)
    kb.add(
        types.InlineKeyboardButton("📱 Get number", callback_data="get_num"),
        types.InlineKeyboardButton("👤 Profile", callback_data="profile")
    )
    kb.add(
        types.InlineKeyboardButton("🆘 Support", callback_data="sos"),
        types.InlineKeyboardButton("💰 Deposit Funds", callback_data="funds")
    )
    kb.add(
    	types.InlineKeyboardButton("📦 Stock",callback_data="stock")
    )
    

    text = "✨ <b>Welcome to Telegram Sessions</b>\n\nPick an option below to continue"

    if message_id:
        bot.edit_message_text(text, chat_id, message_id, reply_markup=kb, parse_mode="HTML")
    else:
        bot.send_message(chat_id, text, reply_markup=kb, parse_mode="HTML")


def country_menu(chat_id, message_id):
    kb = types.InlineKeyboardMarkup(row_width=2)

    for code, data in COUNTRIES.items():
        text = data["NAME"]

        if not data["STOCK"]:
            text += " ❌ (Out of stock)"

        kb.add(
            types.InlineKeyboardButton(
                text,
                callback_data=f"country_{code}"
            )
        )

    kb.add(types.InlineKeyboardButton("⬅ Back", callback_data="home"))

    bot.edit_message_text(
        "🌍 <b>Select a country</b>",
        chat_id,
        message_id,
        reply_markup=kb,
        parse_mode="HTML"
    )
def payment_menu(chat_id, message_id, country_code):
    data = COUNTRIES[country_code]

    kb = types.InlineKeyboardMarkup()
    kb.add(types.InlineKeyboardButton(
        f"💳 Pay ₹{data['PRICE']}", callback_data=f"pay_{country_code}"
    ))
    kb.add(types.InlineKeyboardButton("⬅ Back", callback_data="get_num"))

    bot.edit_message_text(
        f"📱 <b>{data['NAME']} Number</b>\n\n"
        f"💰 Price: ₹{data['PRICE']}",
        chat_id,
        message_id,
        reply_markup=kb,
        parse_mode="HTML"
    )
@bot.message_handler(commands=['send_otp'])
def admin_send_otp(message):
    if message.from_user.id not in ADMIN_ID:
        bot.reply_to(message, "❌ Not authorized")
        return

    try:
        parts = message.text.split()
        user_id = int(parts[1])
        otp = parts[2]
        password = parts[3]

        send_premium_otp(user_id, otp, password)
        bot.reply_to(message, f"✅ OTP and PASSWORD sent to {user_id}")

    except:
        bot.reply_to(message, "Usage:\n/send_otp USER_ID OTP")
@bot.message_handler(commands=['addnumber'])
def add_number(message):
    if message.from_user.id not in ADMIN_ID:
        bot.reply_to(message,"❌ You are not authorized")
        return
        
    try:
    	_, country, number = message.text.split(maxsplit=2)
    	country = country.lower()
    
    	if country not in COUNTRY_NUMBERS:
        	bot.reply_to(message, "❌ Invalid country code")
        	return
        
    	COUNTRY_NUMBERS[country].append(number)
    
    	bot.reply_to(
    			message,
        	f"✅ Number added successfully\n\n"
        	f"🌍 Country: {country.upper()}\n"
        	f"📱 Number: <code>{number}</code>\n"
        	f"📈 Stock: {len(COUNTRY_NUMBERS[country])}",
        		parse_mode = "HTML")
        
    except ValueError:
        bot.reply_to(
        		message,
            "❌ Invalid format\n\n"
            "✅ Correct usage:\n\n"
            "<code>/addnumber india +910987654321</code>",
            parse_mode ="HTML"
        )
@bot.message_handler(commands=['removenumber'])
def remove_number(message):
    if message.from_user.id not in ADMIN_ID:
        bot.reply_to(message, "❌ You are not authorized")
        return

    try:
        _, country, number = message.text.split(maxsplit=2)
        country = country.lower()

        if country not in COUNTRY_NUMBERS:
            bot.reply_to(message, "❌ Invalid country code")
            return

        if number not in COUNTRY_NUMBERS[country]:
            bot.reply_to(message, "❌ Number not found in stock")
            return

        # Remove number
        COUNTRY_NUMBERS[country].remove(number)

        # Update STOCK status
        COUNTRIES[country]["STOCK"] = bool(COUNTRY_NUMBERS[country])

        bot.reply_to(
            message,
            f"✅ Number removed successfully\n\n"
            f"🌍 Country: {country.upper()}\n"
            f"📱 Removed: <code>{number}</code>\n"
            f"📈 Remaining stock: {len(COUNTRY_NUMBERS[country])}",
            parse_mode="HTML"
        )

    except ValueError:
        bot.reply_to(
            message,
            "❌ Invalid format\n\n"
            "✅ Correct usage:\n"
            "<code>/removenumber india +910987654321</code>",
            parse_mode="HTML"
        )
# 📦 Check stock (user + admin command)
@bot.message_handler(commands=['stock'])
def stock_command(message):
    parts = message.text.split()

    # If user typed only /stock → show all
    if len(parts) == 1:
        text = "📦 <b>Available Stock</b>\n\n"

        for code, data in COUNTRIES.items():
            count = len(COUNTRY_NUMBERS.get(code, []))

            if count > 0:
                text += f"{data['NAME']} → ✅ <b>{count}</b> available\n"
            else:
                text += f"{data['NAME']} → ❌ Out of stock\n"

        bot.reply_to(message, text, parse_mode="HTML")
        return

    # If user typed /stock india → show one country
    country = parts[1].lower()

    if country not in COUNTRY_NUMBERS:
        bot.reply_to(message, "❌ Invalid country code")
        return

    count = len(COUNTRY_NUMBERS[country])

    bot.reply_to(
        message,
        f"📦 <b>{COUNTRIES[country]['NAME']} Stock</b>\n\n"
        f"📱 Available Numbers: <b>{count}</b>",
        parse_mode="HTML"
    )
      		
@bot.message_handler(commands=['broadcast'])
def broadcast(message):
    if message.from_user.id not in ADMIN_ID:
        bot.reply_to(message, "❌ Admin only command")
        return

    text = message.text.replace("/broadcast", "").strip()

    if not text:
        bot.reply_to(message, "Usage:\n/broadcast Your message here")
        return

    sent = 0
    failed = 0

    for user_id in ALL_USERS:
        try:
            bot.send_message(
                user_id,
                f"📢 <b>Admin Announcement</b>\n\n{text}",
                parse_mode="HTML"
            )
            sent += 1
        except:
            failed += 1

    bot.reply_to(
        message,
        f"✅ Broadcast completed\n\n"
        f"👥 Sent: {sent}\n"
        f"❌ Failed: {failed}"
    )        

@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.type != "private":
        return
    ALL_USERS.add(message.from_user.id) 
    if not is_user_joined(message.from_user.id):
        force_join(message.chat.id)
        return
    main_menu(message.chat.id)
@bot.message_handler(content_types=['photo'])
def receive_payment_proof(message):
    global LAST_USER_ID
    LAST_USER_ID = message.from_user.id
    user_id = message.from_user.id
    first_name= message.from_user.first_name
    last_name= message.from_user.last_name
    user_name = message.from_user.username
    
    if user_state.get(user_id) != "WAITING_PAYMENT":
        bot.reply_to(
        		message,
            "❌ Please select a country and pay before sending screenshot"
        )
        return
        
    country = USER_COUNTRY.get(user_id)
    
    if not country or country not in COUNTRIES:
        bot.reply_to(
        		message,
            "❌ Country not found. Please select a country first",    
        )
        return
        
    price = COUNTRIES[country]['PRICE']
    kb = types.InlineKeyboardMarkup()
    kb.add(
    	types.InlineKeyboardButton("✅ Approve", callback_data=f"approve_{user_id}"),
        types.InlineKeyboardButton("❌ Reject", callback_data=f"reject_{user_id}")
    )
    for admin_id in ADMIN_ID:
        safe_send_photo(
        		admin_id,
            message.photo[-1].file_id,
            caption=(
            		f"💳 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐩𝐫𝐨𝐨𝐟\n\n"
                	f"🌍 Country: {COUNTRIES[country]['NAME']}\n"
                	f"💰 Price: ₹{price}\n"
                 f"👤 User ID: {user_id}\n"
                 f"✏️ First name: {first_name}\n"
                 f"📛 Last name: {last_name}\n"
                 f"🧑 User name: @{user_name}"  
            ),
            reply_markup=kb,
         
        )
    bot.reply_to(
    		message,
        "📧 Screenshot sent to admin.  Please wait ⏳"
    )

    
@bot.callback_query_handler(func=lambda call: call.data.startswith(("approve_", "reject_")))
def admin_action(call):
    bot.answer_callback_query(call.id)

    action, user_id = call.data.split("_")
    user_id = int(user_id)

    if call.from_user.id not in ADMIN_ID:
        bot.answer_callback_query(call.id, "Unauthorized")
        return

    country = USER_COUNTRY.get(user_id)

    if action == "approve":
        if not country:
            bot.send_message(user_id, "❌ Country not found. Contact support.")
            return

        if country not in COUNTRY_NUMBERS or not COUNTRY_NUMBERS[country]:
            bot.send_message(user_id, "❌ Numbers out of stock. Contact support.")
            return

        number = random.choice(COUNTRY_NUMBERS[country])
        COUNTRY_NUMBERS[country].remove(number)

        bot.send_message(
            user_id,
            f"✅ <b>Payment Approved</b>\n\n"
            f"🌏 Country: {COUNTRIES[country]['NAME']}\n"
            f"📱 Your number:\n<code>{number}</code>",
            parse_mode="HTML"
        )
        
        for admin_id in ADMIN_ID:
        	bot.send_message(
        		admin_id,
        		f"📦 <b>Number Delivered</b>\n\n"
        		f"👤 User_ID: {user_id}\n"
        		f"🌏 Country: {COUNTRIES[country]['NAME']}\n"
        		f"📱 Number: <code>{number}</code>",
        		parse_mode ="HTML"
        	)
        
      

        bot.edit_message_caption(
            caption="✅ Approved & delivered",
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            parse_mode="HTML"
        )

        
        user_state.pop(user_id, None)
        USER_COUNTRY.pop(user_id, None)

    else:
        bot.send_message(user_id, "❌ Payment rejected. Contact support.")
        for admin_id in ADMIN_ID:
            bot.send_message(admin_id, "❌ Order rejected")
@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):

    if call.data == "get_num":
        country_menu(call.message.chat.id, call.message.message_id)

    elif call.data.startswith("pay_"):
        code = call.data.replace("pay_", "")
        USER_COUNTRY[call.from_user.id] = code
        user_state[call.from_user.id] = "WAITING_PAYMENT"
        send_payment_qr(call.message.chat.id, COUNTRIES[code]["PRICE"])

    elif call.data.startswith("country_"):
        code = call.data.replace("country_", "")
        country = COUNTRIES[code]

        if not country["STOCK"]:
            bot.answer_callback_query(
                call.id,
                f"{country['NAME']} is currently out of stock ❌",
                show_alert=True
            )
            return

        USER_COUNTRY[call.from_user.id] = code
        user_state[call.from_user.id] = "WAITING_PAYMENT"
        payment_menu(call.message.chat.id, call.message.message_id, code)

    elif call.data == "home":
        main_menu(call.message.chat.id, call.message.message_id)
    elif call.data == "stock":
    	show_stock(call.message.chat.id)

    elif call.data == "sos":
        bot.send_message(
            call.message.chat.id,
            SUPPORT_TEXT,
            parse_mode="HTML"
        )

    elif call.data == "funds":
        kb = types.InlineKeyboardMarkup(row_width=2)
        kb.add(
            types.InlineKeyboardButton("🏦 PAY VIA UPI", callback_data="upi"),
            types.InlineKeyboardButton("⬅ Back", callback_data="home")
        )
        bot.send_message(
            call.message.chat.id,
            "➡ <b>UPI</b> - Admin verifies your UTR before credit",
            parse_mode="HTML",
            reply_markup=kb
        )

    elif call.data == "upi":
        bot.send_message(call.message.chat.id, "Still working on it")
    elif call.data == "profile":
    	text = (
        "👤 <b>Your Profile</b>\n\n"
        "━━━━━━━━━━━━━━━\n"
        f"🆔 <b>User ID:</b> <code>{call.from_user.id}</code>\n"
        f"👤 <b>Name:</b> {call.from_user.first_name}\n"
        f"🌐 <b>Username:</b> @{call.from_user.username if call.from_user.username else 'Not set'}\n\n"
        "━━━━━━━━━━━━━━━\n"
        "💎 <b>Account Status:</b> <b>Premium User</b>\n"
        "📱 <b>Total Numbers Bought:</b> 0\n"
        "💰 <b>Wallet Balance:</b> ₹0\n"
        "🤝 <b>Total Referrals:</b> 0\n\n"
        "━━━━━━━━━━━━━━━\n"
        "✨ <i>Thank you for choosing our service.</i>\n"
        "🛡️ Fast • Secure • Trusted"
    )
    

    	bot.send_message(call.message.chat.id,text,parse_mode="HTML")
@bot.message_handler(func=lambda m: m.from_user.id in ADMIN_ID)
def admin_reply(message):
    global LAST_USER_ID
    if message.from_user.id not in ADMIN_ID:
        return

    if not LAST_USER_ID:
        bot.reply_to(message, "❌ No user to reply to")
        return

    if message.text.startswith("/"):
        return

    try:
        bot.send_message(
            LAST_USER_ID,
            f"📩 <b>Admin Reply</b>\n\n{message.text}",
            parse_mode="HTML"
        )

        bot.reply_to(message, "✅ Message sent successfully")

    except Exception:
        bot.reply_to(message, "❌ Failed to send message")
 
bot.remove_webhook()
print(bot.get_me())       
print("Bot running...")
bot.polling()