import telebot
import config
from db import get_all_hospitals, get_user_by_name, get_all_appointments_of_user
from states import States

from telebot import types
from telebot import custom_filters

# mongodb link: mongodb+srv://gg:wp@cluster0.2qhvm.mongodb.net/?retryWrites=true&w=majority
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/doc.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🔍List all the hospitals")
    item2 = types.KeyboardButton("📋Show all the appointments")
    item3 = types.KeyboardButton("✉Support service")
    item4 = types.KeyboardButton("→Our website")

    markup.add(item1, item2, item3, item4)

    bot.set_state(message.from_user.id, States.main, message.chat.id)
    bot.send_message(message.chat.id,
                     "Welcome " + "<b>" + message.from_user.first_name + "</b>" + "!\nI'm your own " + "<b>DenSaulyq Manager</b>" + ".".format(
                         message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)


@bot.message_handler(state=States.main)
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "🔍List all the hospitals":
            hospitals = get_all_hospitals()
            msg = ''

            for hospital in hospitals:
                msg += "•" + hospital["naimenovanie_oganizacii"] + ";\n " + hospital["adress"] + ";\n " + hospital[
                    "kontact_tel"] + "\n\n"
            bot.send_message(message.chat.id, msg)
        elif message.text == "📋Show all the appointments":
            bot.send_message(message.chat.id, "Please, write your Name below.")
            bot.set_state(message.from_user.id, States.write_Name, message.chat.id)
        elif message.text == "✉Support service":
            bot.send_message(message.chat.id,
                             "If you have any technical problems, you can contact with our support team:\n •@operator_hike\n •@tunaxxnew\n •@Ecl1ps0")
        elif message.text == "→Our website":
            bot.send_message(message.chat.id, "Here is our website:\n" + "https://densaulyq.me/")
        else:
            bot.send_message(message.chat.id, "Sorry, there is no such command.")


@bot.message_handler(state=States.write_Name)
def IIN(message):
    name = message.text
    if (get_user_by_name(name)):
        print(get_all_appointments_of_user(name))
        bot.send_message(message.chat.id, get_all_appointments_of_user(name))
    else:
        bot.send_message(message.chat.id, "There is no such user.")

    bot.set_state(message.from_user.id, States.main, message.chat.id)


# RUN
bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.polling(none_stop=True)
