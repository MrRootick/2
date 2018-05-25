# -*- coding: utf-8 -*-

import time
import sqlite3
import telebot
import os
from flask import Flask, request

TOKEN = '486750815:AAFQ2XOflRepZFeLJuac-0Ii3vM61ToDg6o'
CHANNEL_NAME = '-1001275366258'

bot = telebot.TeleBot(TOKEN)


def new_post_key():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT asd FROM qweqwe")
        value = c.fetchone()
        key = str(value[0])
        if key != None:
            bot.send_message(CHANNEL_NAME, key)
            c.execute("DELETE FROM qweqwe WHERE asd = '{0}'".format(key))
            conn.commit()
            c.close()
            conn.close()
            time.sleep(60*60)
            new_post_key()
        else:
            time.sleep(60*60)
            new_post_key()
            conn.commit()
            c.close()
            conn.close()
            print("Пусто")
    except:
        print('Какая то ошибка')



@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://botbtc.herokuapp.com/' + TOKEN)
    return "!", 200

if __name__ == '__main__':
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
    new_post_key()
