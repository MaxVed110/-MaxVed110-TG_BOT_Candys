from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ConversationHandler
import tg_commander
import logger_new

if __name__ == '__main__':

    logger_new.logger_cls()

    updater = Updater('5433876542:AAHm2Ui64wlqht70EtD9FPJWBMJ8Kz66Cb8')
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', tg_commander.start_game_bot)
    game_handler = ConversationHandler(
        entry_points=[CommandHandler('game', tg_commander.start), CommandHandler('return', tg_commander.start)],
        states={
            tg_commander.USER_STEP: [MessageHandler(filters.Filters.text & (~filters.Filters.command), tg_commander.game_step)]
        },
        fallbacks=[CommandHandler('exit', tg_commander.exit_user)]
    )

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(game_handler)

    updater.start_polling()
    updater.idle()

