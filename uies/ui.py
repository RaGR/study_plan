def start_ui(message, types, bot):
    pass


def contact_ui(message, types, bot):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="share my contact", request_contact=True)
    markup.add(button_phone)
    bot.send_message(message.chat.id, "please share your contact for being in touch", reply_markup=markup)


def channel_joined_ui(message, types, bot):
    chat_id = message.chat.id

    markup = types.InlineKeyboardMarkup()

    button_join = types.InlineKeyboardButton(
        text="Join Channel", url="https://t.me/zabansarareyinstitute"
    )

    button_joined = types.InlineKeyboardButton(
        text="check", callback_data="joined_channel"
    )
    markup.add(button_join, button_joined)

    bot.send_message(chat_id, welcome_text, reply_markup=markup)


welcome_text = (
    "به *ربات تلگرامی آموزشگاه زبان سرا* خوش آمدید\n\n"
    "برای استفاده از ربات، لطفاً ابتدا به کانال ما بپیوندید.\n\n"
    "بعد از پیوستن به کانال، /start را دوباره بزنید.\n\n"
)
