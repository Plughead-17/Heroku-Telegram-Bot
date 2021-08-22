import bot
import misc
import network
import telebot
import os
from flask import Flask, request

server = Flask(__name__)

bot_1 = telebot.TeleBot(misc.TELEGRAM_TOKEN)

def Test():
#    page = network.get_page_confirm(misc.URL)
#    items = parser.get_content(page)
    bot.sendmessagebot("hi")
##########################################################################

######################
#   start
@bot_1.message_handler(commands = ["start"])
def start(message):
    bot_1.reply_to(message, "hello, " + message.from_user.first_name)

######################
#
@bot_1.message_handler(func = lambda message: True, content_types = ["text"])
def echo(message):
    bot_1.reply_to(message, message.text)

######################
#
@server.route('/' + misc.TELEGRAM_TOKEN, methods = ["POST"])
def get_message():
    string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(string)
    bot_1.process_new_updates([update])
    return '|', 200

######################
#
@server.route('/')
def webhook():
    bot_1.remove_webhook()
    bot_1.send_wbhook(url = misc.URL_APP)
    return '|', 200

##########################################################################
#       Main
def main():
    print("Start APP!")
    server.run(host = "0.0.0.0", port = int(os.environ.get("PORT", 5000)))
#    bot.RunRunFastUCan()

##########################################################################
if __name__ == "__main__":
    main() # - action