from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater, Filters, CallbackContext, MessageHandler, CallbackQueryHandler, CommandHandler
from handler import start,tekshir
import os

TOKEN = "6004154698:AAEo2pZT8WqoCqRGAXZchoYMtdgozcq3Kbc"

updater = Updater(token=TOKEN)

dp = updater.dispatcher
dp.add_handler(CommandHandler('start',start))
dp.add_handler(CallbackQueryHandler(tekshir,pattern='tekshirish'))
updater.start_polling()
updater.idle()