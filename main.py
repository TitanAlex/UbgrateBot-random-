import telebot
import random

bot = telebot.TeleBot('1412005435:AAH-APcKTRVve8hMAci6Zh_S_J5QvPsIXq0')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('/help')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('/go')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('a', 'b', 'c')

keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('d', 'e', 'f')

keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.row('g', 'h', 'i')

keyboard6 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard6.row('j', 'k', 'l')

coopybook = {
    'j': 'Неправильно',
    'k': 'Неправильно',
    'l': 'Правильно\nТы победил! Наверное...',
    'привет': 'Привет',
    'пока': 'Пока',
}

sticker = {
    1: 'CAACAgEAAxkBAAEBs_Bf4D4Yc6BNJQ7-ylaJCAABDDcB6egAAjoJAAK_jJAEdBjCoBMxYzkeBA',
    2: 'CAACAgEAAxkBAAEBs_Jf4D4a9t6B12sHba_G6l6gKC7cJgACRgkAAr-MkAQ7mcTuV6DCsx4E',
    3: 'CAACAgEAAxkBAAEBs_Rf4D4dvmPEWhYwpNfAcWswzA0Q2gACSgkAAr-MkAT0cmmwpQ8wXB4E',
    4: 'CAACAgEAAxkBAAEBtrdf5OJohN_SDJDLwmHy0AABEwABgQEyAAInCQACv4yQBNQdmAgvlnzeHgQ',
    5: 'CAACAgIAAxkBAAEBtrlf5OOVOkYykpqi6q_UrQrrAX35GgACSgEAApafjA6Mfk73uDljvh4E',
    6: 'CAACAgIAAxkBAAEBtrtf5OPc78JArK8t2kpX0qKcUSe5TwACTAEAApafjA74EwWV2_gQrB4E',

}

coins = {
    1: 'Орёл🦅',
    2: 'Решка🌰',
}


@bot.message_handler(commands=['start'])
def start_start(start):
    bot.send_message(start.chat.id, 'Привет, приятно познакомиться', reply_markup=keyboard1)


@bot.message_handler(commands=['help'])
def start_help(help):
    bot.send_message(help.chat.id, 'Привет, я пришел тебе на помощь, вот список моих команд:')
    bot.send_message(help.chat.id, '\n /help - 📑список команд.'
                                   '\n /start - ❤проверить мой пульс.'
                                   '\n /Christmas - 🎄поздравить с Новым Годом!'
                                   '\n /update - 💹последнее обновление бота'
                                   '\n /play - 🎮поиграть с ботом'
                                   '\n /cube - 🎲кинуть кубик(0-100)'
                                   '\n /coin - 👛бросить монетку')


@bot.message_handler(commands=['update'])
def start_update(update):
    bot.send_message(update.chat.id, 'Можете кинуть кубик🎲 /cube\nИли кинуть монетку 👛/coin ')


@bot.message_handler(commands=['cube'])
def cube(cube):
    bot.send_message(cube.chat.id, 'Наше число...')
    bot.send_message(cube.chat.id, str(random.randint(0, 100)))


@bot.message_handler(commands=['play'])
def start_play(play):
    bot.send_message(play.chat.id, 'Привет, давай поиграем в игру "Отгадай значение"', reply_markup=keyboard2)


@bot.message_handler(commands=['go'])
def start_go(go):
    bot.send_message(go.chat.id, 'Что такое "Канитель"?\n a. Суета, излишняя торопливость'
                                 '\n b. Металлическая нить для вышивания\n c. Сильный морской ветер',
                     reply_markup=keyboard3)


@bot.message_handler(content_types=['text'])
def start_message(message):
    print(message)

    name = coopybook.get(message.text.lower())
    print(name)

    rand = random.randint(1, 6)
    print(rand)

    coin = random.randint(1, 2)
    print(coin)

    if message.text.lower() == '/coin':
        bot.send_message(message.chat.id, coins.get(coin))


    if message.text.lower() == '/christmas':
        bot.send_sticker(message.chat.id, sticker.get(rand))

    if message.text.lower() == 'c':
        bot.send_message(message.from_user.id, '\nНеправильно\nСледующий вопрос...'
                                               '\nЧто такое "Сермяга"?\nd. Грубое некрашенное сукно'
                                               '\ne. Неопрятный человек\nf. Нижняя мужская рубаха',
                         reply_markup=keyboard4)

    elif message.text.lower() == 'a':
        bot.send_message(message.from_user.id, '\nНеправильно\nСледующий вопрос...'
                                               '\nЧто такое "Сермяга"?\nd. Грубое некрашенное сукно'
                                               '\ne. Неопрятный человек\nf. Нижняя мужская рубаха',
                         reply_markup=keyboard4)

    elif message.text.lower() == 'b':
        bot.send_message(message.from_user.id, '\nПравильно\nСледующий вопрос...'
                                               '\nЧто такое "Сермяга"?\nd. Грубое некрашенное сукно'
                                               '\ne. Неопрятный человек\nf. Нижняя мужская рубаха',
                         reply_markup=keyboard4)

    elif message.text.lower() == 'd':
        bot.send_message(message.from_user.id, '\nПравильно\nСледующий вопрос...'
                                               '\nЧто такое "Кукомоя"?\ng. Кулак, сжатая ладонь'
                                               '\nh. Неряха, неопрятный человек\ni. Кувшин для умывания',
                         reply_markup=keyboard5)

    elif message.text.lower() == 'e':
        bot.send_message(message.from_user.id, '\nНеправильно\nСледующий вопрос...'
                                               '\nЧто такое "Кукомоя"?\ng. Кулак, сжатая ладонь'
                                               '\nh. Неряха, неопрятный человек\ni. Кувшин для умывания',
                         reply_markup=keyboard5)

    elif message.text.lower() == 'f':
        bot.send_message(message.from_user.id, '\nНеправильно\nСледующий вопрос...'
                                               '\nЧто такое "Кукомоя"?\ng. Кулак, сжатая ладонь'
                                               '\nh. Неряха, неопрятный человек\ni. Кувшин для умывания',
                         reply_markup=keyboard5)

    elif message.text.lower() == 'g':
        bot.send_message(message.from_user.id, '\nНеправильно\nСледующий вопрос...'
                                               '\nЧто такое "Кукомоя"?\ng. Кулак, сжатая ладонь'
                                               '\nh. Неряха, неопрятный человек\ni. Кувшин для умывания',
                         reply_markup=keyboard5)

    elif message.text.lower() == 'h':
        bot.send_message(message.from_user.id, '\nПравильно\nСледующий вопрос...'
                                               '\nЧто такое "Рюма"?\nj. Человек, несущий чушь '
                                               '\nk. Глубокий сосуд для напитков \nl. Плакса, рыдающий человек',
                         reply_markup=keyboard6)

    elif message.text.lower() == 'i':
        bot.send_message(message.from_user.id, '\nНеправильно\nСледующий вопрос...'
                                               '\nЧто такое "Рюма"?\nj. Человек, несущий чушь '
                                               '\nk. Глубокий сосуд для напитков \nl. Плакса, рыдающий человек',
                         reply_markup=keyboard6)

    if name:
        bot.send_message(message.from_user.id, name)


@bot.message_handler(content_types=['sticker'])
def sticker_id(sticker):
    print(sticker)


bot.polling(none_stop=True, interval=0)
