from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater, Filters, CallbackContext, MessageHandler, CallbackQueryHandler, CommandHandler
from handler import start,tekshir,download
import os

TOKEN = "5696117143:AAH3Ej-BE4VgykO6NlKHUxYDQISbN85CzR0"

updater = Updater(token=TOKEN)

dp = updater.dispatcher
dp.add_handler(CommandHandler('start',start))
dp.add_handler(CallbackQueryHandler(tekshir,pattern='tekshirish'))
dp.add_handler(MessageHandler(Filters.update,download))
updater.start_polling()
updater.idle()