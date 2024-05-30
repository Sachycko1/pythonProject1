import telebot # Импортируем библиотеку для написания тг бота
from telebot import types # Импортируем модуль для определения типов для объектов тг
import random # Импортируем модуль рандомайзера
from library import module # Импортируем модуль для использования значений карт Таро
from layout_lib import layout # Иммпортируем модуль для использования схем раскладов таро

tarot_ThreeCards = layout.ThreeCards # Присваиваем переменной список ThreeCards
tarot_FullCup = layout.FullCup # Присваиваем переменной список FullCup
tarot_CelticCross = layout.CelticCross # Присваиваем переменной список CelticCross
Tarot_Cards = module.cards # Присваиваем переменной список cards

bot = telebot.TeleBot('6806588578:AAGN92P9oSov7x96oxCZ1HqDOnI8Q1BfY-o') # ТОКЕН

# Список команд бота
commands = [
    '/help',
    '/start',
    '/variants',
    '/ThreeCards',
    '/CelticCross',
    '/FullCup'
]

# Создаем обработчик сообщений команды /help
@bot.message_handler(commands=['help'])
def help(message):

# Создаем клавиатуру с кнопками
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1) # Создаем экземпляр разметки клавиатуры с параметрами: корректные (подстраиваются под размер экрана), количество кнопок в строке = 1
    start = types.KeyboardButton('/start')
    variants = types.KeyboardButton('/variants')
    help = types.KeyboardButton('/help')
    markup.add(start, variants, help)
    bot.send_message(message.chat.id, "Выберите кнопку", reply_markup=markup) # Отправляем сообщение пользователю с разметкой клавиатуры

# Создаем обработчик сообщений команды /start
@bot.message_handler(commands=['start'])
def start(message):
    mess = (f'Здравствуй, <b>{message.from_user.first_name}</b>, я бот <u>RyderWaiteTarot</u>, и я могу сделать тебе бесплатный расклад!\n'
            f'Но прежде чем его сделать, задумайся какой вопрос тебя беспокоит, а также знай, что карты не расскажут что-либо на "Да" или "Нет".\n'
            f'Пиши <b>/variants</b>, чтобы узнать какие расклады я могу делать.\n'
            f'Если ты не знаешь какие команды здесь есть, пиши <b>/help</b>')
    bot.send_message(message.chat.id, mess, parse_mode='html')

# Создаем обработчик сообщений команды /variants
@bot.message_handler(commands=['variants'])
def variants(message):
    variants_text = """
/ThreeCards - Три карты. Самый простой расклад который описывает положение прошлого, настоящего и будущего.\n
/CelticCross - Кельтский крест. Простой расклад, для более глубокого анализа какой-либо ситуации.\n
/FullCup - Полная чаша. Простой расклад, для анализа финансовой ситуации.
    """
    bot.send_message(message.chat.id, variants_text)

# Создаем обработчик сообщений команды /ThreeCards
@bot.message_handler(commands=['ThreeCards'])
def question(message):
    mess = bot.send_message(message.chat.id, "Какой вопрос, Вас, интересует?")
    bot.register_next_step_handler(mess, ThreeCards)
def ThreeCards(message):
    bot.send_message(message.chat.id,'Вот Ваш расклад:')
    for card in tarot_ThreeCards:
        bot.send_message(message.chat.id, card['talk'])  # Выводит краткую речь
        bot.send_photo(message.chat.id, card['photo'])  # Выводит схему
    for i in random.sample(Tarot_Cards, 3):  # Выбирает 3 рандомных библиотеки с картами
        bot.send_photo(message.chat.id, i['photo'])  # Выводит карту
        bot.send_message(message.chat.id, i['name'])  # Выводит название карты
        mess = (f"<u>Карта в плюсе:</u>\n {i['meaning_up']}\n<u>Карта в минусе:</u>\n {i['meaning_rev']}") # Переменная с описанием карт
        bot.send_message(message.chat.id, mess, parse_mode='html')  # Выводит описание карты в плюсе и минусе

# Создаем обработчик сообщений команды /CelticCross
@bot.message_handler(commands=['CelticCross'])
def question(message):
    mes = bot.send_message(message.chat.id, "Какой вопрос, Вас, интересует?")
    bot.register_next_step_handler(mes, CelticCross)

def CelticCross(message):
    bot.send_message(message.chat.id, 'Вот Ваш расклад:')
    for card in tarot_CelticCross:
        bot.send_message(message.chat.id, card['talk'])  # Выводит краткую речь
        bot.send_photo(message.chat.id, card['photo'])  # Выводит схему
    for i in random.sample(Tarot_Cards, 10): # Выбирает 10 рандомных библиотек с картами
        bot.send_photo(message.chat.id, i['photo'])  # Выводит карту
        bot.send_message(message.chat.id, i['name'])  # Выводит название карты
        mess = (f"<u>Карта в плюсе:</u>\n {i['meaning_up']}\n<u>Карта в минусе:</u>\n {i['meaning_rev']}") # Переменная с описанием карт
        bot.send_message(message.chat.id, mess, parse_mode='html')  # Выводит описание карты в плюсе и минусе

# Создаем обработчик сообщений команды /FullCup
@bot.message_handler(commands=['FullCup'])
def question(message):
    mes = bot.send_message(message.chat.id, "Какой вопрос, Вас, интересует?")
    bot.register_next_step_handler(mes, FullCup)

def FullCup(message):
    bot.send_message(message.chat.id, 'Вот Ваш расклад:')
    for card in tarot_FullCup:
        bot.send_message(message.chat.id, card['talk'])  # Выводит краткую речь
        bot.send_photo(message.chat.id, card['photo'])  # Выводит схему
    for i in random.sample(Tarot_Cards, 4):  # Выбирает 4 рандомных библиотеки с картами
        bot.send_photo(message.chat.id, i['photo'])  # Выводит карту
        bot.send_message(message.chat.id, i['name'])  # Выводит название карты
        mess = (f"<u>Карта в плюсе:</u>\n {i['meaning_up']}\n<u>Карта в минусе:</u>\n {i['meaning_rev']}") # Переменная с описанием карт
        bot.send_message(message.chat.id, mess, parse_mode='html')  # Выводит описание карты в плюсе и минусе

# Запуск работы бота
bot.polling(none_stop=True)
