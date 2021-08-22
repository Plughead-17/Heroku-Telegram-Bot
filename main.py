import bot
import misc
import network
import telebot
import os
from flask import Flask, request, render_template

server = Flask(__name__)

TELEGRAM_TOKEN = "1822171895:AAGizcD8jcNdWrKgAmKhzSsqUZyo-n07kEU"
URL_APP = "https://telegram-bot-pyhon-test0001.herokuapp.com/"  + TELEGRAM_TOKEN

bot_1 = telebot.TeleBot(TELEGRAM_TOKEN)

def Test():
#    page = network.get_page_confirm(misc.URL)
#    items = parser.get_content(page)
    bot.sendmessagebot("hi")

######################
#   start
@bot_1.message_handler(commands = ["start"])
def start(message):
    print("bot_1.message_handler(commands = [start])")
    print("def start(message):")
    bot_1.reply_to(message, "hello, " + message.from_user.first_name)

######################
#
@bot_1.message_handler(func = lambda message: True, content_types = ["text"])
def echo(message):
    print("bot_1.message_handler(func = lambda message: True, content_types = [text])")
    print("def echo(message):")
    bot_1.reply_to(message, message.text)

######################
#
@server.route('/' + TELEGRAM_TOKEN, methods = ["POST"])
def get_message():
    print("server.route('/' + TELEGRAM_TOKEN, methods = [POST])")
    print("def get_message():")
    string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(string)
    bot_1.process_new_updates([update])
    return '|', 200

######################
#
@server.route('/')
def webhook():
    print("\nПервый старт\n")
    return '''<h1>/token?mass=</h1>'''
#       /token?mass=

@server.route("/test")
def test():
    print("\nInput !!!\n")

    ms = request.args.get("mass")
    if ms == "usd":
        page = network.get_page_confirm(misc.URL)
        ms = bot.get_content(page)
        return '''  {}  
                    Покупка = {}
                    Продажа = {}'''.format(ms[0], ms[1], ms[2])

#@server.route('/')
#def hello_world():
#    print("\n\n\n\ndef hello_world():\n\n\n")
#    return render_template('index.html')

@server.route("/onliner")
def onliner():
    return bot.onliner_parce()

##########################################################################
#       Main
def main():
    print("Start APP!")
    server.run(host = "0.0.0.0", port = int(os.environ.get("PORT", 5000)))
#    bot.RunRunFastUCan()

##########################################################################
if __name__ == "__main__":
    main() # - action