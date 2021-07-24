# TODO: REFACTOR THIS SHIT SOMETIME LATER

import telebot
import os
import random
import dotenv

dotenv.load_dotenv()
token = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(token, parse_mode=None)

markup = telebot.types.ReplyKeyboardMarkup()
cat = telebot.types.KeyboardButton('KIT')
dog = telebot.types.KeyboardButton('пЕс')
markup.add(cat, dog)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    msg = 'кіт, пес або пішов на хуй?\nвипробуй успіх - натисни на кнопку!'
    bot.send_message(message.chat.id, msg, reply_markup=markup)

# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)

def generate_num():
    num = random.randint(0,1)
    return num

def user_input(message):
    if message.text == 'KIT':
        num = 0
    if message.text == 'пЕс':
        num = 1
    return num

def choose_pic(f):
    path = f
    files = os.listdir(path)
    chosen_pic = random.choice(files)
    return chosen_pic

@bot.message_handler(func=lambda m: True)
def send_photo(message):
    r_num = generate_num()
    u_num = user_input(message)
    if r_num == u_num:
        if u_num == 0:
            pic = choose_pic('cats')
            photo = open(f'cats/{pic}', 'rb')
            msg = 'перемога!!!! \nудача виявилася на твоєму боці !!!!!\n але чи пощастить тобі наступного разу?!?!?!??!'
            bot.send_photo(message.chat.id, photo, msg)
        else:
            pic = choose_pic('dogs')
            photo = open(f'dogs/{pic}', 'rb')
            msg = 'перемога!!!! \nудача виявилася на твоєму боці !!!!!\n але чи пощастить тобі наступного разу?!?!?!??!'
            bot.send_photo(message.chat.id, photo, msg)
    else:
        pic = choose_pic('fus')
        photo = open(f'fus/{pic}', 'rb')
        msg = 'ІДИ НА ХУЙ!!!!!'
        bot.send_photo(message.chat.id, photo, msg)
    # if  message.text == 'KIT':
    #     photo = open('thumb2-small-french-bulldog-funny-animals-dogs-puppy-pets.jpg', 'rb')
    #     bot.send_photo(message.chat.id, photo)
    # else:
    #     bot.send_message(message.chat.id, 'ты пидр')


bot.polling()
        # photo = open('fu.jpg', 'rb')
            # photo = open('doog.jpg', 'rb')
            # photo = open('poop.jpg', 'rb')