# -*- coding: utf-8 -*-
import os
import time
import sqlite3
import telebot
import random
from flask import Flask, request

TOKEN = '486750815:AAFQ2XOflRepZFeLJuac-0Ii3vM61ToDg6o'
CHANNEL_NAME = '-1001275366258'

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


def new_post_key():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        q=random.randint(1,47000)
        c.execute("SELECT asd FROM qqq WHERE id='{}'".format(q))
        value = c.fetchone()
        key = str(value[0])
        if key != None:
            bot.send_message(CHANNEL_NAME, key)
            c.close()
            conn.close()
            time.sleep(60*10)

        else:
            time.sleep(10)
            c.close()
            conn.close()
            print("Пусто")
    except:
        print('Какая то ошибка')




@bot.message_handler(commands=['start'])  # Обработка команды start
def handle_text(message):
    answer = "Привет"
    bot.send_message(message.chat.id, answer )




@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://botch.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    new_post_key()
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))