import network
from filesystem import msg
import parser
import misc
import time

###########################################################################
REQUESTS_BOT = "https://api.telegram.org/bot" + misc.TELEGRAM_TOKEN
CHATID = "841721020"
SEND_MESSAGE = REQUESTS_BOT + "/sendmessage?chat_id=" + CHATID + "&text="
GET_ME = REQUESTS_BOT + "/getMe"
UPDATE = REQUESTS_BOT + "/getUpdates"

##########################################################################
#       Сообщение от бота
def getmessagebot():
    page = network.get_html(UPDATE)
    if page.status_code == 200:
        return page.json()
    if page.status_code == 404:
        msg("Error status_code = 404 - def getmessagebot() - get_html(UPDATE)")
        return 0
    return 0

##########################################################################
#       Сообщеие боту
def sendmessagebot(message = "Wait a second, please"):
    page = network.get_html(SEND_MESSAGE + message)
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
             #   print(data)
                if first_work_time == False:
                    if data["text"] == "/test_key":
                        page = network.get_page_confirm(misc.URL)
                        items = parser.get_content(page)
                        sendmessagebot(str(items[0])+ "\nПокупка - " + str(items[2])+ "\nПродажа - " +items[1])
#                        sendmessagebot("https://baraholka.onliner.by/viewtopic.php?t=24715013")
                else:
                    first_work_time = False

        ###############################################

        time.sleep(3)