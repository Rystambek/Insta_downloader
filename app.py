from telegram.ext import Updater, CommandHandler, MessageHandler, Filters,CallbackQueryHandler,Dispatcher
from telegram import Update,Bot
from handler import (start,
                     tekshir,
                     download
                     )
from flask import Flask, request
import os

# get token from environment variable
TOKEN = '6004154698:AAEo2pZT8WqoCqRGAXZchoYMtdgozcq3Kbc'

bot = Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/webhook', methods=["POST", "GET"])
def hello():
    if request.method == 'GET':
        return 'hi from Python2022I'
    elif request.method == "POST":
        data = request.get_json(force = True)
        
        dp: Dispatcher = Dispatcher(bot, update_queue=None, workers=0)
        update:Update = Update.de_json(data, bot)
        
        dp.add_handler(CommandHandler('start',start))
        dp.add_handler(CallbackQueryHandler(tekshir,pattern='tekshirish'))
        dp.add_handler(MessageHandler(Filters.update,download))


        
        dp.process_update(update)
        return 'ok'