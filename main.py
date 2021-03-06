import bot
import filesystem
import misc
import network
import telebot
import os
import time
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

server = Flask(__name__)
#CORS(server)
TELEGRAM_TOKEN = "1822171895:AAGizcD8jcNdWrKgAmKhzSsqUZyo-n07kEU"
URL_APP = "https://telegram-bot-pyhon-test0001.herokuapp.com/"

bot_1 = telebot.TeleBot(TELEGRAM_TOKEN)

def Test(message):
#    page = network.get_page_confirm(misc.URL)
#    items = parser.get_content(page)
    bot.sendmessagebot(message)

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
        return '''  {}<br>  
                    Продажа = {}<br>
                    Покупка = {}<br>
                    '''.format(ms[0], ms[1], ms[2])

@server.route("/onliner")
def onliner():
    return bot.onliner_parce()

@server.route("/te")
@cross_origin()
def autoria():
    yer = int(time.asctime()[-4:])


    items = request.args.values()
    print("---------------------\nКоличество параметров")

    print(type(items))

    mass = []
    for item in items:
        if item == '':
            return ''' Error! NO parameter '''

        mass.append(str(item))

    print(str(len(mass)))
    category = mass[0]
    fuel = mass[1]
    origin = mass[2]
    age = mass[3]
    age = yer - int(age)

    if age >= 15:
        age = "gt15"
    else:
        age = "lt" + str(age)

    price = str(mass[4])
    engine = str(mass[5])

    req = misc.GENERAL_REQUEST +"category=" +category +"&fuel=" +fuel +"&origin=" +origin +"&age=" +age +"&price=" +price +"&engine=" +engine

    print("-----------------------")
    print(req)
    print("-----------------------")
    resp = network.get_html(req)
    resp = resp.json()["newPrices"]
    return resp


@server.route("/autoria")
@cross_origin()
def auto():

    yer = int(time.asctime()[-4:])

    items = request.args.values()
    mass = []
    for item in items:
        if item == '':
            return ''' Error! NO parameter '''

        mass.append(str(item))

    category = mass[0]
    fuel = mass[1]
    origin = mass[2]
    age = mass[3]
    age = yer - int(age)
    if age >= 15:
        age = "gt15"
    else:
        age = "lt" + str(age)
    price = str(mass[4])
    engine = str(mass[5])

    req = misc.GENERAL_REQUEST +"category=" +category +"&fuel=" +fuel +"&origin=" +origin +"&age=" +age +"&price=" +price +"&engine=" +engine

    print("-----------------------")
    print(req)
    print("-----------------------")
    resp = network.get_html(req)
    resp = resp.json()["newPrices"]
    return resp

# входной

# category=1    // категория автотранспорта (точно) 1- автомобили 2- мотоциклы
# &fuel=1       // топливо (точно) 1- бензин 2- дизель 6- электро 5- гибрид
# &origin=3     // страна происхождения (точно) 1- другие 2- ЕАСТ 3- ЕС 4- канада
# &age=gt15     // возраст машины lt1 - lt14 - от 1 до 14ти | gt15 от 15ти и более
# &price=5000   // цена зарубедом от 100
# &engine=6000  // объём двигателя

# выходной

# https://auto.ria.com/content/news/calculateAuto/?
# category=1    // категория автотранспорта (точно) 1- автомобили 2- мотоциклы
# &fuel=1       // топливо (точно) 1- бензин 2- дизель 6- электро 5- гибрид
# &origin=3     // страна происхождения (точно) 1- другие 2- ЕАСТ 3- ЕС 4- канада
# &age=gt15     // возраст машины lt1 - lt14 - от 1 до 14ти | gt15 от 15ти и более
# &price=5000   // цена зарубежом от 100
# &engine=6000  // объём двигателя

#    return'''
# категория -------------------------------------- {}<br>
# топливо ---------------------------------------- {}<br>
# страна происхождения --------------------------- {}<br>
# возраст машины --------------------------------- {}<br>
# цена зарубедом --------------------------------- {}<br>
# объём двигателя -------------------------------- {}<br>
# '''.format(mass["category"], mass["fuel"], mass["origin"], mass["age"], mass["price"], mass["engine"])

#1    "importDuty": 275,		        // Ввозная пошлина
#2    "exciseDuty": 9000,	            // акцизный сбор
#3    "VAT": 2855,		                // НДС
#4    "bondedCarCost": 5000,	        // Стоимость зарубежом
#5    "customsClearanceCosts": 12130,	// Растаможка
#6    "clearedCarsCost": 17130	        // Стоимость с разтоможкой

##########################################################################
#       Main
def main():
    print("Start APP!")
    server.run(host = "0.0.0.0", port = int(os.environ.get("PORT", 5000)))

##########################################################################
if __name__ == "__main__":
    main() # - action

# __5 параметров
# Вид топлива           (gas, dis, el, gib)
# Страна происхождения  (other, eact, ec, can)
# Год выпуска           (любое число)
# Изначальная стоимость (любое число)
# объём двигателя       (любое число)