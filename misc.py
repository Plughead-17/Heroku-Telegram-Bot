HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
           "Accept": '*/*'}

TELEGRAM_TOKEN = "1822171895:AAGizcD8jcNdWrKgAmKhzSsqUZyo-n07kEU"
URL_APP = f"https://telegram-bot-pyhon-test0001.herokuapp.com/{TELEGRAM_TOKEN}"
bad_symbols = "!@<>|\?"

###########################################################################
REQUESTS_BOT = "https://api.telegram.org/bot" + TELEGRAM_TOKEN
CHATID = "841721020"
SEND_MESSAGE = REQUESTS_BOT + "/sendmessage?chat_id=" + CHATID + "&text="
GET_ME = REQUESTS_BOT + "/getMe"
UPDATE = REQUESTS_BOT + "/getUpdates"
###########################################################################
URL = "https://kurs.onliner.by/"

LOG_FILE = "log.log"