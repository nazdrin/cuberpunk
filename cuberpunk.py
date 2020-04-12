import telebot
import conf
import random
from telebot.types import ReplyKeyboardMarkup
import time
from telebot.types import ReplyKeyboardMarkup
number =()
bot = telebot.TeleBot('1013913913:AAGL1cZniJEBg3yBRbelebzW-QcP4bfzTxs')
i=5

@bot.message_handler(commands=['start'])
def handle_start(message):
    global number
    number = (random.randint(1, 25))

    global i
    i=5
    send = bot.send_message(message.from_user.id,'Привет, как тебя зовут?')
    bot.register_next_step_handler(send, gf)
def gf(message):
    b=message.text
    bot.send_message(message.from_user.id,'Привет, '+ b + ', приятно познакомиться!!!☺\n\n\n Я загадал для тебя число от 1 до 25!')
    bot.send_message(message.from_user.id, b + ', ты должен угадать его за 5 попыток😃\n\n\n\n\nУдачи!!!')
    d=bot.send_message(message.from_user.id, 'Введи число!')
    bot.register_next_step_handler(d,gc)
def gc(message):
    global i
    i -= 1
    if i==-1:
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        keyboard.row('Новая игра')
        send = bot.send_message(message.from_user.id,'К сожелению ти проиграл,чтоби начать новую игру,нажми на кнопку:"Новая игра"' , reply_markup= keyboard)
        bot.register_next_step_handler(send,handle_start )


    else:
        b= str (i)
        try:
            a = int(message.text)
            if a == number:
                keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

                keyboard.row('Новая игра')
                bot.send_sticker(message.from_user.id,'CAACAgIAAxkBAAJEkl6S4UyTDxKd2dyJ1TPJLBc99uhtAAInAAOvxlEalWaeHhh77REYBA')
                send=bot.send_message(message.from_user.id, 'Поздравляю,ты угадал!', reply_markup= keyboard)

                bot.register_next_step_handler(send, handle_start)
            elif a < number:

                send = bot.send_message(message.from_user.id, ('Маловато , у тебя осталось '+b+' попыток'))
                bot.register_next_step_handler(send, gc)

            elif a > number:

                send=bot.send_message(message.from_user.id, ('Многовато будет, у тебя осталось '+b+ ' попыток'))
                bot.register_next_step_handler(send, gc)

        except:
            list =('Ошибка. Введи число! У тебя осталось '+b+' попыток')
            list2 = ('Ты ввёл что-то, а нужно цифры. у тебя осталось '+b+' попыток')
            list3 =('ну-ну, у тебя осталось '+b+' попыток')
            a=[list,list2,list3]
            b=random.choice(a)
            send=bot.send_message(message.from_user.id, b)
            bot.register_next_step_handler(send, gc)
bot.polling(none_stop=True)