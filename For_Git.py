import telebot
import config

first = ''
second = ''
third = ''

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Ну что же, {message.from_user.first_name} {message.from_user.last_name}, приветствую тебя! Меня зовут Великий Квадратный Уравнитель! Давай-ка посмотрим что тут у тебя. Нажми любую кнопку.'
    bot.send_message(message.chat.id, mess)

@bot.message_handler(func=lambda m: True)
def answer_msg(message):
    if message.text:
        bot.send_message(message.chat.id, 'Отлично! Для начала введи значение для параметра "a"')
        bot.register_next_step_handler(message, reg_int_a)

def reg_int_a(message):
    global first
    first = float(message.text)
    bot.send_message(message.chat.id, f'a = {message.text}. Теперь введи b = ')
    bot.register_next_step_handler(message, reg_int_b)

def reg_int_b(message):
    global second
    second = float(message.text)
    bot.send_message(message.chat.id, f'Так b = {message.text}, Осталось ввести c = ')
    bot.register_next_step_handler(message, reg_int_c)

def reg_int_c(message):
    global third
    third = float(message.text)
    a = first
    b = second
    c = third
    Disc = b**2 - 4*a*c
    if Disc > 0:
        x_1 = round(((-b - Disc ** 0.5) / (2 * a)), 4)
        x_2 = round(((-b + Disc ** 0.5) / (2 * a)), 4)
        bot.send_message(message.chat.id,'Дискриминант =' + str(Disc) + ', ' + 'x_1 =' + str(x_1) + ', ' + 'x_2 =' + str(x_2))
    elif Disc == 0:
        x_1 = round((-b / (2 * a)), 4)
        bot.send_message(message.chat.id,'Дискриминант = 0 в уравнении один корень x =' + str(x_1))
    elif Disc < 0:
        bot.send_message(message.chat.id,'Дискриминант меньше нуля, в уравнении нет корней,  значит нет и действительных решений')
    else:
        bot.send_message(message.chat.id,'Что-то пошло не так, дружок')

def whatelse():
    pass