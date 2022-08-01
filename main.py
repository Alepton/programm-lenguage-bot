import telebot
from telebot import types

bot = telebot.TeleBot('5415648861:AAHA_ZlgFYFYrDPsKLPhFD6eQ7CC7a2vlPI')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Cоздание игр')
    btn2 = types.KeyboardButton('Мобильные приложения')
    btn3 = types.KeyboardButton('Веб разработка')
    btn4 = types.KeyboardButton('Софт для компьютеров')
    btn5 = types.KeyboardButton('Обработка данных')
    btn6 = types.KeyboardButton('Создание ИИ')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    send_mess = f"<b>Привет {message.from_user.first_name} {message.from_user.last_name}</b>\nКакое направление тебя интересует?"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['website'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Поcетить сайт", url="https://itproger.com/courses/"))
    bot.send_message(message.chat.id, "Отличный выбор, нажмите на кнопку и начинайте изучение курсов прямо сейчас",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(commands=['vk'])
def open_website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Поcетить группу ВК", url="https://vk.com/prog_life/"))
    bot.send_message(message.chat.id, "Отличный выбор, нажмите на кнопку и погрузитесь в мир IT прямо сейчас",
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "cоздание игр":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Под мобильные телефоны')
        btn2 = types.KeyboardButton('Компьютеры и консоли')
        btn3 = types.KeyboardButton('Виртуальная реальность')
        btn4 = types.KeyboardButton('Web игра')
        markup.add(btn1, btn2, btn3, btn4)
        final_message = "Определитесь с направлением. Выберите из списка"

    elif get_message_bot == "под мобильные телефоны":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('2D игры')
        btn2 = types.KeyboardButton('3D игры')
        markup.add(btn1, btn2)
        final_message = "Какой тип игры вы бы хотели разрабатывать?"

    elif get_message_bot == "2d игры":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Подходящие курсы", url="https://itproger.com/tag/unity/"))
        final_message = "Реализация мобильных игр намного удобнее при помощи игровых движков. Для создания 2D игр под мобильные устройства стоит использовать игровой движок Unity или Godot. Они позволяют создавать игры сразу под несколько платформ (iOS, Android) и обладают большим набором функционала."

    elif get_message_bot == "3d игры":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Подходящие курсы", url="https://itproger.com/tag/unity/"))
        final_message = "Реализация мобильных игр намного удобнее при помощи игровых движков. Для создания 2D игр под мобильные устройства стоит использовать игровой движок Unity или Godot. Они позволяют создавать игры сразу под несколько платформ (iOS, Android) и обладают большим набором функционала."


    elif get_message_bot == "мобильные приложения":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('IOS')
        btn2 = types.KeyboardButton('Андороид')
        markup.add(btn1, btn2)
        final_message = "Под какую платформу вы хотите писать программы?"

    elif get_message_bot == "ios":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Подходящие курсы", url="https://itproger.com/course/swift/"))
        final_message = "Разработка приложений и игр для iOS и Macintosh производится на языке Swift. Язык продвигается компанией Apple, поэтому его популярность постоянно растет. Язык имеет простой синтаксис, удобную среду разработки и большую функциональность, что позволяет создавать проекты любой сложности."

    elif get_message_bot == "андроид":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Подходящие курсы", url="https://itproger.com/tag/java/"))
        final_message = "Java - удобный, быстрый и многофункционалный язык, который подходит для множества сфер, начиная от веба и заканчивая созданием игр под мобильные устройства и ПК."

    elif get_message_bot == "веб разработка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Внешний вид сайта (front-end)')
        btn2 = types.KeyboardButton('Работа с сервером (backend)')
        markup.add(btn1, btn2)
        final_message = "Чем бы вы хотели заниматься?"

    elif get_message_bot == "внешний вид сайта (front-end)":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Подходящие курсы", url="https://itproger.com/tag/javascript/"))
        final_message = "Внешний вид сайта, Front-end, не состоит из лишь одного языка программирования. Для создания внешней части сайта необходимо изучить как минимум: HTML, CSS, SASS, Gulp, Bootstrap и JavaScript."

    elif get_message_bot == "работа с сервером (backend)":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Подходящие курсы", url="https://itproger.com/tag/csharp/"))
        final_message = "Многие крупные компании любят использовать более традиционный и надежный подход для создания сайтов, поэтому используют язык Ruby, C# или же Java. Определитесь какой язык вам больше подходит по синтаксису и изучайте именно его."


    elif get_message_bot == "софт для компьютеров":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Windows')
        btn2 = types.KeyboardButton('Mac')
        btn3 = types.KeyboardButton('Все платформы')
        markup.add(btn1, btn2, btn3)
        final_message = "Под какую платформу вы хотите разрабатывать?"

    elif get_message_bot == "windows":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Подходящие курсы", url="https://itproger.com/tag/csharp/"))
        final_message = "Язык C# был разработан компанией Microsoft и он идеально подходит для создания программ под Windows. Компания Microsoft всячески продвигает язык, обновляет его и разрабатывает большиство своих приложений на нём. Изучение C# позволит вам создавать программы под Windows и запускать их на любом компьютере с ОС Microsoft."

    elif get_message_bot == "mac":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Подходящие курсы", url="https://itproger.com/course/swift/"))
        final_message = "Разработка приложений и игр для iOS и Macintosh производится на языке Swift. Язык продвигается компанией Apple, поэтому его популярность постоянно растет. Язык имеет простой синтаксис, удобную среду разработки и большой набор функций, что позволяет создавать проекты любой сложности."

    elif get_message_bot == "все платформы":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Подходящие курсы", url="https://itproger.com/tag/java/"))
        final_message = "Java - удобный, быстрый и многофункционалный язык, который может выполняться вне зависимости от операционной системы: Windows, Mac или Linux."


    elif get_message_bot == "обработка данных":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Подходящие курсы", url="https://itproger.com/tag/python/"))
        final_message = "Python обладает большим набором библиотек, позволяющих обрабатывать большие потоки информации. Изучение Python для данной сферы считается наиболее хорошим вариантом, так как в Интернете вы найдете много обучающего материала, а сам язык не составит для вас больших проблем в плане изучения."

    elif get_message_bot == "создание ИИ":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Подходящие курсы", url="https://itproger.com/tag/python/"))
        final_message = "Python – хороший язык для разработки искусственного интеллекта. Язык легкий, удобный и многофункциональный. Его с легкостью можно применять для создания прототипов ИИ. Разработка ИИ базируется на написании математических формул, просчете данных и построении математической модели для принятия решений. Изучив Python вы не научитесь создавать умные ИИ, так как вам потребуются еще хорошие знания в математике. Тем не менее, благодаря языку вы сможете описывать всю логику и функции ваших программ."

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        btn1 = types.KeyboardButton('Cоздание игр')
        btn2 = types.KeyboardButton('Мобильные приложения')
        btn3 = types.KeyboardButton('Веб разработка')
        btn4 = types.KeyboardButton('Софт для компьютеров')
        btn5 = types.KeyboardButton('Обработка данных')
        btn6 = types.KeyboardButton('Создание ИИ')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        final_message = "Что-то пошло не так) Выберите направление, нажав кнопку ниже"

    bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)


bot.polling(none_stop=True)
