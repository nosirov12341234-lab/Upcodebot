import asyncio
import logging
import os
import threading
from flask import Flask
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

# Logging sozlamalari
logging.basicConfig(level=logging.INFO)

# Flask veb-server (Botni 24/7 ishlatish uchun)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot ishlayapti!"

def run_flask():
    # Replit odatda 8080 portni kutadi, lekin 5000 ham ishlaydi. 
    # Foydalanuvchi 8080 so'ragan.
    app.run(host='0.0.0.0', port=8080)

# Bot sozlamalari
BOT_TOKEN = os.environ.get('BOT_TOKEN')

# Botni yaratish
if BOT_TOKEN:
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2))
else:
    logging.error("BOT_TOKEN topilmadi!")
    bot = None

dp = Dispatcher()

# Tugmalar (Inline Keyboard)
def get_language_keyboard():
    keyboard = [
        [InlineKeyboardButton(text="Python 🐍", callback_data="lang_python"),
         InlineKeyboardButton(text="JavaScript 📜", callback_data="lang_js")],
        [InlineKeyboardButton(text="C++ ⚙️", callback_data="lang_cpp"),
         InlineKeyboardButton(text="SQL 🗄️", callback_data="lang_sql")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)

# Komanda xandlerlari
@dp.message(Command("start"))

# muoliflik huquqlqri buzilmasin