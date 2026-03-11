import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Bot is running on Render 🚀")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, message.text)

print("Bot is running...")

bot.infinity_polling()