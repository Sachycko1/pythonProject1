import random
import telebot # Импортируем модуль для написания тг бота
from telebot import types # Импортируем модуль для определения типов для объектов тг
from db_library import db_module # Импортируем модуль для использования значений карт Таро
from layout_lib import layout # Иммпортируем модуль для использования схем раскладов таро

tarot_ThreeCards = layout.ThreeCards # Присваиваем переменной список ThreeCards
tarot_FullCup = layout.FullCup # Присваиваем переменной список FullCup
tarot_CelticCross = layout.CelticCross # Присваиваем переменной список CelticCross
Tarot_Cards = db_module.cards # Присваиваем переменной список cards

bot = telebot.TeleBot('6806588578:AAGN92P9oSov7x96oxCZ1HqDOnI8Q1BfY-o') # ТОКЕН

# Список команд бота
commands = [
    '/start',
    '/help',
    '/variants',
    '/ThreeCards',
    '/CelticCross',
    '/FullCup'
]

# Создаем обработчик сообщений для команды /help
@bot.message_handler(commands=['help'])
def help(message):

# Создать клавиатуру с кнопками
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) # Создаем экземпляр разметки клавиатуры с параметрами: однострочные (кнопки), количество кнопок в строке = 1
    start = types.KeyboardButton('/start')
    variants = types.KeyboardButton('/variants')
    help = types.KeyboardButton('/help')
    markup.add(start, variants, help)
    bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=markup) # Отправляем сообщение пользователю с разметкой клавиатуры

# Создаем обработчик сообщений для команды /start
@bot.message_handler(commands=['start'])
def start(message):
    mess = (f'Здравствуй, <b>{message.from_user.first_name}</b>, я бот <u>RyderWaiteTarot</u>, и я могу сделать тебе бесплатный расклад! Но прежде чем его сделать, задумайся какой вопрос тебя беспокоит, а также знай, что карты не расскажут что-либо на "Да" или "Нет".\n'
            f'Пиши <b>/variants</b>, чтобы узнать какие расклады я могу делать. Если ты не знаешь какие команды здесь есть, пиши <b>/help</b>')
    bot.send_message(message.chat.id, mess, parse_mode='html')

# Создаем обработчик сообщений для команды /variants
@bot.message_handler(commands=['variants'])
def variants(message):
    variants_text = """
/ThreeCards - Три карты. Самый простой расклад который описывает положение прошлого, настоящего и будущего.\n
/CelticCross - Кельтский крест. Простой расклад, для более глубокого анализа какой-либо ситуации.\n
/FullCup - Полная чаша. Простой расклад, для анализа финансовой ситуации.
    """
    bot.send_message(message.chat.id, variants_text)


# Создаем обработчик сообщений для команды /ThreeCards
@bot.message_handler(commands=['ThreeCards'])
def ThreeCards(message):
    for card in tarot_ThreeCards:
        bot.send_message(message.chat.id, card['talk'])  # Выводит краткую речь
        bot.send_photo(message.chat.id, card['photo'])  # Выводит схему
    for i in random.sample(Tarot_Cards, 3):  # Выбирает 3 рандомных библиотеки с картами
        bot.send_photo(message.chat.id, i['photo'])  # Выводит карту
        bot.send_message(message.chat.id, i['name'])  # Выводит название карты
        bot.send_message(message.chat.id,f"Карта в плюсе:\n {i['meaning_up']}\nКарта в минусе:\n {i['meaning_rev']}")  # Выводит описание карты в плюсе и минусе


# Создаем обработчик сообщений для команды /CelticCross
@bot.message_handler(commands=['CelticCross'])
def CelticCross(message):
    for card in tarot_CelticCross:
        bot.send_message(message.chat.id, card['talk'])  # Выводит краткую речь
        bot.send_photo(message.chat.id, card['photo'])  # Выводит схему
    for i in random.sample(Tarot_Cards, 10): # Выбирает 10 рандомных библиотек с картами
        bot.send_photo(message.chat.id, i['photo'])  # Выводит карту
        bot.send_message(message.chat.id, i['name'])  # Выводит название карты
        bot.send_message(message.chat.id,f"Карта в плюсе:\n {i['meaning_up']}\n Карта в минусе:\n {i['meaning_rev']}")  # Выводит описание карты в плюсе и минусе

# Создаем обработчик сообщений для команды /FullCup
@bot.message_handler(commands=['FullCup'])
def FullCup(message):
    for card in tarot_FullCup:
        bot.send_message(message.chat.id, card['talk'])  # Выводит краткую речь
        bot.send_photo(message.chat.id, card['photo'])  # Выводит схему
    for i in random.sample(Tarot_Cards, 4):  # Выбирает 4 рандомных библиотеки с картами
        bot.send_photo(message.chat.id, i['photo'])  # Выводит карту
        bot.send_message(message.chat.id, i['name'])  # Выводит название карты
        bot.send_message(message.chat.id,f"Карта в плюсе:\n {i['meaning_up']}\n Карта в минусе:\n {i['meaning_rev']}")  # Выводит описание карты в плюсе и минусе

# Запускаем работу бота
bot.polling(none_stop=True)
