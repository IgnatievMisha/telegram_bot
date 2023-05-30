import random
import telebot
from telebot import types

f=open('facts.txt', 'r', encoding='UTF-8')
facts=f.read().split('\n')
f.close()

f=open('thinks.txt', 'r', encoding='UTF-8')
thinks=f.read().split('\n')
f.close()

bot=telebot.TeleBot("5801592663:AAGgvqMhPIP97nY0INbroJ2cnnv1O2AJnE0")
@bot.message_handler(commands=['start'])
def start(m, res=False):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Fact")
    item2=types.KeyboardButton("Think")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, "Push Button", reply_markup=markup)

'''def start_message(message):
    bot.send_message(message.chat.id, "Hello")'''
@bot.message_handler(content_types=['text'])
def handler_text(message):
    if message.text.strip()=='Fact':
        answer=random.choice(facts)
    elif message.text.strip()=='Think':
        answer=random.choice(thinks)
    bot.send_message(message.chat.id, answer)
bot.polling()