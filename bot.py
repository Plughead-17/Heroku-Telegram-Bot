import requests
import time
import misc
import network
import json
from bs4 import BeautifulSoup
import filesystem

# RunRunFastUCan

class Rabbit:
    pass


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
#       Сообщение от бота
def getmessagebot():
    page = network.get_html(misc.UPDATE)
    if page.status_code == 200:
        return page.json()
    if page.status_code == 404:
        return 0
    return 0

##########################################################################
#       Сообщеие боту
def sendmessagebot(message = "Wait a second, please"):
    page = network.get_html(misc.SEND_MESSAGE + message)
    return page



def RunRunFastUCan():

    i = 50
    data = {
        "update_id": "---"
    }
    first_time = True

    while True:
        ###############################################
        temp = getmessagebot()
        # ----------------------------------------------

        if temp["ok"] == "True":
            print(temp["ok"])

        if temp == 0:
            print("Test" + str(i))
            i -= 1
            if i == 0:
                return 0
        # ----------------------------------------------
        else:
            filesystem.msg(temp)
            if len(temp["result"]) == 0:
                print("break")
                break
            if temp["result"][-1]["update_id"] != data["update_id"]:
               data = {
                   "update_id": temp["result"][-1]["update_id"],
                   "message_id": temp["result"][-1]["message"]["message_id"],
                   "chat_id": temp["result"][-1]["message"]["chat"]["id"],
                   "text": temp["result"][-1]["message"]["text"]
               }
#            if first_time == False:
#                temp1(temp)
##################################################################
        print()
        print("　　　　　 |＞　 フ ")
        print("　　　　　|  0 0  |")
        print("　 　　　／ミ x_ 彡")
        print("　　 　 /　　　 　 |")
        print("　　　 /　 ヽ　　 ﾉ")
        print("　／￣|　　 |　|　|")
        print("　| (￣ヽ＿_ヽ_)_)")
        print("　＼二つ")
##################################################################
        time.sleep(3)

###########################################################
def temp1(data):
    if data["text"] == "/test_key":
        page = network.get_page_confirm(misc.URL)
        items = get_content(page)
        item = str(items[0]) + "\nПокупка - " + str(items[2]) + "\nПродажа - " + str(items[1])
        sendmessagebot(item)
    else:
        return False

    ###############################################
    time.sleep(3)