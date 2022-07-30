import telebot
from telebot import types

bot = telebot.TeleBot('5415648861:AAHA_ZlgFYFYrDPsKLPhFD6eQ7CC7a2vlPI')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('Cоздание игр')
    btn2 = types.KeyboardButton('Мобильные приложения')
    btn3 = types.KeyboardButton('Веб разработка')
    btn4 = types.KeyboardButton('Обработка данных')
    markup.add(btn1, btn2, btn3, btn4,)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>\nКакой язык?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Поcетить сайт", url="https://itproger.com/"))
    bot.send_message(message.chat.id, "Отличный выбор", parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['vk'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Поcетить сайт", url="https://itproger.com/"))
    bot.send_message(message.chat.id, "Отличный выбор", parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "cоздание игр":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Под мобильные телефоны')
        btn2 = types.KeyboardButton('Компьютеры и консоли')
        btn3 = types.KeyboardButton('Виртуальная реальность')
        markup.add(btn1, btn2, btn3,)
        final_message = "Определитесь с направлением. Выберите из списка"
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Под мобильные телефоны')
        btn2 = types.KeyboardButton('Компьютеры и консоли')
        btn3 = types.KeyboardButton('Виртуальная реальность')
        markup.add(btn1, btn2, btn3, )
        final_message = "Что-то пошло не так) Выберите направление"

    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)





bot.polling(none_stop=True)
