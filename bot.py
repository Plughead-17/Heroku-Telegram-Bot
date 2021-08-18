import requests
import time

###########################################################################
TELEGRAM_TOKEN = "1822171895:AAGizcD8jcNdWrKgAmKhzSsqUZyo-n07kEU"

URL = "https://kurs.onliner.by/"
####################
HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
           "Accept": '*/*'}


###########################################################################
REQUESTS_BOT = "https://api.telegram.org/bot" + TELEGRAM_TOKEN
CHATID = "841721020"
SEND_MESSAGE = REQUESTS_BOT + "/sendmessage?chat_id=" + CHATID + "&text="
GET_ME = REQUESTS_BOT + "/getMe"
UPDATE = REQUESTS_BOT + "/getUpdates"
######################################
##########################################################################
#       Получить старницу с сайта
def get_html(url, params = None):   # Запрос на сайт
    return requests.get(url, headers = HEADERS, params = params)

##########################################################################
#       Проаерить статус коды
def get_page_confirm(url):   # Запрос на сайт
    page = get_html(url)
    if page.status_code == 404:
        return 0
    return page
#######################################

from bs4 import BeautifulSoup

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
    page = get_html(UPDATE)
    if page.status_code == 200:
        return page.json()
    if page.status_code == 404:
        return 0
    return 0

##########################################################################
#       Сообщеие боту
def sendmessagebot(message = "Wait a second, please"):
    page = get_html(SEND_MESSAGE + message)
    return page

def func():

    i = 50
    data = {
        "update_id": "---"
    }
    first_work_time = True


    while True:
        ###############################################
        temp = getmessagebot()
        # ----------------------------------------------
        if temp == 0:
            i -= 1
            if i == 0:
                return 0
        # ----------------------------------------------
        else:
            if temp["result"] == 0:
                break
            if temp["result"][-1]["update_id"] != data["update_id"]:

                data = {
                    "update_id": temp["result"][-1]["update_id"],
                    "message_id": temp["result"][-1]["message"]["message_id"],
                    "chat_id": temp["result"][-1]["message"]["chat"]["id"],
                    "text": temp["result"][-1]["message"]["text"]
                }
                print(data)
                if first_work_time == False:
                    if data["text"] == "/test_key":
                        page = get_page_confirm(URL)
                        items = get_content(page)
                        sendmessagebot(str(items[0])+ "\nПокупка - " + str(items[2])+ "\nПродажа - " +items[1])
#                        sendmessagebot("https://baraholka.onliner.by/viewtopic.php?t=24715013")
                else:
                    first_work_time = False

        ###############################################
        time.sleep(3)