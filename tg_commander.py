import random
import logger_new
from telegram import Update
from telegram.ext import ConversationHandler

count = 35
user_step: int
ii_step: int
info: str

USER_STEP, GAME_ERROR = range(2)


def start_game_bot(update: Update, _):
    global info

    info = f'{update.message.from_user.first_name}' + ', ' + f'{update.message.from_user.id}'

    logger_new.logger.info(f'Пользователь // {info} // вошёл в чат')

    update.message.reply_text('Привет! Готов начать игру?\n\nВ игре тебе будет необходимо брать '
                              'конфеты, отправляя в сообщении их количество.\n'
                              'Побеждает тот, кто первым забирает последнюю конфету\n'
                              '/game - начать игру\n'
                              '/return - начать сначала\n'
                              '/exit - закончить игру')


def start(update: Update, _):

    logger_new.logger.info('Start')

    update.message.reply_text('Осталось 35 конфет.\nВведи количество конфет, которое хочешь взять')
    return USER_STEP


def game_step(update: Update, _):
    #принимает сообщение юзера от start, главный цикл игры

    global user_step
    global ii_step
    global count

    user_step = update.message.text
    if user_step.isdigit():
        if 1 <= int(user_step) <= 5:
            count = count - int(user_step)
        else:

            logger_new.logger.error('Некорректное число')

            update.message.reply_text(f'Тебе необходимо взять от 1 до 5 конфет.\nВведи корректное число')
            update.message.reply_text(f'Введи количество конфет, которое хочешь взять')
            return USER_STEP
    else:

        logger_new.logger.error('Некорректное сообщение')

        update.message.reply_text(f'Тебе необходимо взять от 1 до 5 конфет.\nВведи корректное число')
        update.message.reply_text(f'Введи количество конфет, которое хочешь взять')
        return USER_STEP

    ii_step = random.randint(1, 6)
    update.message.reply_text(f'Осталось {count} конфет')
    if count <= 0:
        update.message.reply_text(f'Ты победил!')
        return ConversationHandler.END
    count = count - ii_step
    update.message.reply_text(f'Бот взял {ii_step} конфет.\nОсталось {count} конфет')
    if count <= 0:
        update.message.reply_text(f'Ты проиграл!')
        return ConversationHandler.END
    update.message.reply_text(f'Введи количество конфет, которое хочешь взять')
    return USER_STEP


def exit_user(update: Update, _):

    #выход из бота, конец диалога

    logger_new.logger.info(f'Пользователь // {info} // вышел из чата')

    update.message.reply_text('Игра окончена.\nЧтобы начать заново, введи /game')
