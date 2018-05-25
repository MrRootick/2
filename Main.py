# -*- coding: utf-8 -*-

import time
import sqlite3
import telebot


BOT_TOKEN = '486750815:AAFQ2XOflRepZFeLJuac-0Ii3vM61ToDg6o'
CHANNEL_NAME = '-1001275366258'

bot = telebot.TeleBot(BOT_TOKEN)


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





if __name__ == '__main__':
    new_post_key()
    bot.polling(none_stop=True, timeout=1200)
