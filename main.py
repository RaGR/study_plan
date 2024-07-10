import telebot
from telebot import types
from functions.funcs import contact_check, is_in_channel, read_data_uniq
from uies.ui import contact_ui, channel_joined_ui

TOKEN = "6932315200:AAGz-7mqMYgj238aw_tkgyEj2M-rtzbKyQk"

# bot username : test313777bot
id_channel_zabansara = "@zabansarareyinstitute"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    user_data = read_data_uniq(str(message.chat.id))

    if user_data is False:
        contact_ui(message, types, bot)

    elif is_in_channel(bot, id_channel_zabansara, message.chat.id) is False:
        channel_joined_ui(message, types, bot)


@bot.message_handler(content_types=['contact'])
def contact_handler(message):
    if contact_check(message):
        if is_in_channel(bot, id_channel_zabansara, message.chat.id):
            start_ui(message, types, bot)

        else:
            channel_joined_ui(message, types, bot)


bot.polling()
