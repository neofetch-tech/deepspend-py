import telebot
TOKEN = '8632394479:AAGgpgi7WSgSym8QjeaQ8nx1j38jd8FKdHM'

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello! I am DeepSpend, bot in Telegram, nice to meet you!')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'I am DeepSpend, only a simple bot, but I am trying to be useful!\n\n')

bot.polling(none_stop=True)