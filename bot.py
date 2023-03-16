from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater, Filters, CallbackContext, MessageHandler, CallbackQueryHandler, CommandHandler
import os

TOKEN = os.environ('TOKEN')

updater = Updater(token=TOKEN)

dp = updater.dispatcher

updater.start_polling()
updater.idle()