import os
from flask import Flask
from threading import Thread
import telebot
from telebot import types

app = Flask(__name__)

@app.route('/')
def home():
    return "I'm alive!"

def run_webserver():
    # Используем динамический порт для Railway
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    thread = Thread(target=run_webserver)
    thread.start()

# Получаем токен бота из переменных окружения
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Логируем значение токена для отладки (не выводить токен в продакшн!)
print(f"Token is: {repr(TELEGRAM_BOT_TOKEN)}")

if TELEGRAM_BOT_TOKEN is None:
    raise ValueError("Please set the TELEGRAM_BOT_TOKEN in environment variables.")
    
# Убираем лишние пробелы
TELEGRAM_BOT_TOKEN = TELEGRAM_BOT_TOKEN.strip()

# Проверяем наличие пробелов в токене
if ' ' in TELEGRAM_BOT_TOKEN:
    raise ValueError("Token must not contain spaces")

# Создаем экземпляр бота
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Visit The Website', url='https://Rocketlikes.com')
    markup.add(button)
    bot.send_message(message.chat.id, "Hi! That is an assistant bot! Here is the website:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def fallback_handler(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text='Visit The Website', url='https://Rocketlikes.com')
    markup.add(button)
    bot.send_message(message.chat.id, "Hi! That is an assistant bot! Here is the website:", reply_markup=markup)

if __name__ == "__main__":
    keep_alive()
    bot.polling(non_stop=True)
