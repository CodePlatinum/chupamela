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
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    thread = Thread(target=run_webserver)
    thread.start()

TELEGRAM_BOT_TOKEN = os.getenv("T8194602621:AAFBOIzunPMVScHsvBqEfbaGkF57vJJJ_-E
")
if TELEGRAM_BOT_TOKEN is None:
    raise ValueError("Please set the TELEGRAM_BOT_TOKEN in environment variables.")

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
    bot.remove_webhook()
    bot.polling(non_stop=True)
