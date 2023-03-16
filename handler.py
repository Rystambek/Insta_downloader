from telegram import Update,ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import Updater, Filters, CallbackContext, MessageHandler, CallbackQueryHandler, CommandHandler
import requests

def start(update:Update,context:CallbackContext):
    bot = context.bot
    chat_id = update.message.chat.id
    text = "⛔️ *Botdan to'liq foydalanish uchun* quyidagi kanallarga obuna bo'ling"
    chanel_1 = "https://t.me/Rustambek03_IT_blog"
    chanel_2 = "https://t.me/Rustambek15649"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton('➕ kanalga qo\'shilish',url = chanel_1),InlineKeyboardButton('➕ kanalga qo\'shilish',url = chanel_2)],
        [InlineKeyboardButton('Tekshirish',callback_data='tekshirish')],
        ],
    )
    bot.sendMessage(chat_id,text,reply_markup=keyboard,parse_mode="MarkdownV2")

def tekshir(update:Update, context:CallbackContext):
    bot = context.bot
    query = update.callback_query
    chat_id = query.message.chat.id
    user_name = query.message.chat.first_name
    message_id = query.message.message_id
    user_id = query.from_user.id
    chanel_1 = 'https://t.me/Rustambek03_IT_blog'
    chanel_2 = 'https://t.me/Rustambek15649'
    chanel1 = bot.getChatMember(f"@{chanel_1[13:]}",chat_id)['status']
    chanel2 = bot.getChatMember(f"@{chanel_2[13:]}",chat_id)['status']
    print(chanel1)
    print(chanel2)
    if chanel1!='left' and chanel2!='left':
        text = f"""🔥 Xush kelibsiz {user_name}, Bot orqali yuklab olishingiz mumkin:

• Instagram - stories, post va IGTV;
• YouTube - video/audio istalgan formatda;
• TikTok - suv belgisiz video;
• Likee - suv belgisiz video;

🚀 Media yuklashni boshlash uchun uning havolasini yuboring.
😎 Bot guruhlarda ham ishlay oladi!"""
        bot.edit_message_text(chat_id=user_id,text=text,message_id=message_id,parse_mode="MarkdownV2")

    else:
        text = "Kanallarga a'zo bo'lmadingiz"
        keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton('➕ kanalga qo\'shilish',url = chanel_1),InlineKeyboardButton('➕ kanalga qo\'shilish',url = chanel_2)],
        [InlineKeyboardButton('Tekshirish',callback_data='tekshirish')],
        ]
    )
        bot.edit_message_text(chat_id=user_id,text=text,message_id=message_id,reply_markup=keyboard,parse_mode="MarkdownV2")
    
