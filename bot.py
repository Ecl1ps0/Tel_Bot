import telebot
import config

from telebot import types

# mongodb link: mongodb+srv://gg:wp@cluster0.2qhvm.mongodb.net/?retryWrites=true&w=majority
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/doc.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🔍List all the hospitals")
    item2 = types.KeyboardButton("📋Show all the appointments")
    item3 = types.KeyboardButton("✉Support service")
    item4 = types.KeyboardButton("→Our website")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, "Welcome " + "<b>" + message.from_user.first_name + "</b>" + "!\nI'm your own " + "<b>DenSaulyq Manager</b>" + ".".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "🔍List all the hospitals":
            bot.send_message(message.chat.id, "...")
        elif message.text == "📋Show all the appointments":
            bot.send_message(message.chat.id, "...")
        elif message.text == "✉Support service":
            bot.send_message(message.chat.id, "If you have any technical problems, you can contact with our support team:\n •@operator_hike\n •@tunaxxnew\n •@Ecl1ps0")
        elif message.text == "→Our website":
            bot.send_message(message.chat.id, "Here is our website:\n" + "https://densaulyq.me/")

# RUN
bot.polling(none_stop=True)
