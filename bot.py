import requests
import time
import misc
import network
import json
from bs4 import BeautifulSoup
import filesystem
import json
import telebot

# RunRunFastUCan

class Rabbit:
    pass

bot_1 = telebot.TeleBot(misc.TELEGRAM_TOKEN)
########################
#       Get Soup
def get_soup(page):
    if page:
        return BeautifulSoup(page.text, "html.parser")

########################
#       Parse now
def get_content(page):
    contents = get_soup(page)
    items = contents.find(class_="b-currency-table__more")
    items = items.find_all("td")
    i = 0
    for item in items:
        i += 1
        if item.text == 'ул. Некрасова, 3а (магазин "Виталюр")':
            mass = []
            mass.append(item.text)
            mass.append(items[i -2].text)
            mass.append(items[i -3].text)

    return mass

#    soup = BeautifulSoup(page.text, "html.parser")
#    item = soup.find("table").find_next("table")
# 'ул. Некрасова, 3а (магазин "Виталюр")'

###########################################################################
#       Message from bot
def getmessagebot():
    page = network.get_html(misc.UPDATE)
    if page.status_code == 200:
        return page.json()
    if page.status_code == 404:
        return 0
    return 0

##########################################################################
#       Send message to bot
def sendmessagebot(message = "Wait a second, please"):
    page = network.get_html(misc.SEND_MESSAGE + message)
    return page


###########################################################
#
def RunRunFastUCan():
    i = 50
    first_time = True
    data = {
        "update_id": "---"
    }
#-----------------------------------------------------
    while True:
        ###############################################
        temp = getmessagebot()
        # ----------------------------------------------
#        if temp["ok"] == True:
#            print("\n" + str(temp["ok"]) + "Test mass\n")

        # ----------------------------------------------
        # ----------------------------------------------
        if temp == 0:
            i -= 1
            if i == 0:
                print("End timeout")
                return 0
            time.sleep(3)
        # ----------------------------------------------
        if len(temp["result"]) == 0:
            print("No messages.")
        else:

            if temp["result"][-1]["update_id"] != data["update_id"]:
                data = {
                    "update_id": temp["result"][-1]["update_id"],
                    "message_id": temp["result"][-1]["message"]["message_id"],
                    "chat_id": temp["result"][-1]["message"]["chat"]["id"],
                    "date": temp["result"][-1]["message"]["date"],
                    "text": temp["result"][-1]["message"]["text"]
                }
                if first_time == True:
                    first_time = False
                else:
                    if data["text"] == "/usd":
                        send_data()
                    if data["text"] == "/catsme":
                        cat_1()
        time.sleep(3)

###########################################################
#
def send_data():
    page = network.get_page_confirm(misc.URL)
    items = get_content(page)
    item = str(items[0]) + "\nПокупка - " + str(items[2]) + "\nПродажа - " + str(items[1])
    sendmessagebot(item)

###########################################################
#
def cat_1():
##################################################################
    item = ":　　　　　 |＞　 フ \n:　　　　　|  0 0  |\n:　 　　　／ミ x_ 彡\n:　　 　 /　　　 　 |\n:　　　 /　 ヽ　　 ﾉ\n:　／￣|　　 |　|　|\n:　| (￣ヽ＿_ヽ_)_)\n:　＼二つ"
    sendmessagebot(item)
##################################################################