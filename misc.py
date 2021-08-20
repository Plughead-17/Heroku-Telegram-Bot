import socket
import os
#################################
TEST_PATH_SOURCE = "Новая папка/Новая папка (2)/"
TEST_PATH_DESTINATION = "Новая папка/Новая папка/"
#################################

HEADERS = {"user-agent": "Mozilla/5.0 (Windows NT 10; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
           "Accept": '*/*'}

TELEGRAM_TOKEN = "1822171895:AAGizcD8jcNdWrKgAmKhzSsqUZyo-n07kEU"

TITLE_PROGRAMM = "ONLINER.BY"

OSNAME = os.name
HOSTNAME = socket.gethostname()
LOGINNAME = os.getlogin()

###########################################################################
REQUESTS_BOT = "https://api.telegram.org/bot" + TELEGRAM_TOKEN
CHATID = "841721020"
SEND_MESSAGE = REQUESTS_BOT + "/sendmessage?chat_id=" + CHATID + "&text="
GET_ME = REQUESTS_BOT + "/getMe"
UPDATE = REQUESTS_BOT + "/getUpdates"
###########################################################################

if OSNAME == "nt":
    SYSDIR = "C://"
    DOWNLOAD = "O://"

    CINEMA = "K://"
    MUSIC = "F://"
    DISTRIBUTIV = "N://"
    DOCS = "L://"
    VIDEO = "H://"

    LOG_FILE = DOWNLOAD + "UserData/PythonProjects/TelegramBotTest001/log.txt"

if OSNAME == "posix":
    SYSDIR = "//home/"
    DOWNLOAD = "//srv/dev-disk-by-label-sds/download/"
    MASSIVE = "//srv/dev-disk-by-id-wwn-0x600605b003c59d60279481993488b075-part1/"

    CINEMA = MASSIVE + "Cinema"
    MUSIC = MASSIVE + "music"
    DISTRIBUTIV = MASSIVE + "distributiv"
    DOCS = MASSIVE + "docs"
    VIDEO = MASSIVE + "video"

    LOG_FILE = "O:/UserData/PythonProjects/TelegramBotTest001/log.txt"
###########################################################################
#       Парсер
REQUESTS_GARBAGE = "https://baraholka.onliner.by/"
REQUESTS_SEARCH = "search.php?q="

KORPUSA_TEXT = "Поиск в разделе «Корпуса. Блоки питания. ИБП(UPS). Системы охлаждения. Моддинг.»"
KORPUSA = "&f=181"

MATCPU_TEXT = "Поиск в разделе «Материнские платы. Процессоры»"
MATCPU = "&f=285"

# Поиск в разделе «Оперативная память»
MEMORY = "&f=1676"

VIDEOCARD_TEXT = "Поиск в разделе «Видеокарты»"
VIDEOCARD = "&f=286"

HARDISK_TEXT = "Поиск в разделе «SSD. HDD. USB Flash. Карты памяти»"
HARDISK = "&f=184"

MONITOR_TEXT = "Поиск в разделе «Мониторы. Проекторы.»"
MONITOR = "&f=185"

TEST_MASS = [
    "USER1", "USER2", "USER3",    "USER1", "USER2", "USER3",    "USER1", "USER2", "USER3",
    "TEST1", "TEST2"
]

LABEL_MASS = [
"Поиск в разделе «Корпуса. Блоки питания. ИБП(UPS). Системы охлаждения. Моддинг.»",
"Поиск в разделе «Видеокарты»",
"Поиск в разделе «Материнские платы. Процессоры»",
"Поиск в разделе «Оперативная память»",
"Поиск в разделе «Мониторы. Проекторы.»",
"Поиск в разделе «SSD. HDD. USB Flash. Карты памяти»"
]
SMAL_LBEL_MASS = [
"Корпуса/Охлады",
"Видеокарты",
"Процы/Платы",
"Память",
"Мониторы",
"SSD/HDD"

]

REQUEST_MASS = [
"&f=181",   # Поиск в разделе «Корпуса. Блоки питания. ИБП(UPS). Системы охлаждения. Моддинг.»
"&f=286",   # Поиск в разделе «Видеокарты»
"&f=285",   # Поиск в разделе «Материнские платы. Процессоры»
"&f=1676",  # Поиск в разделе «Оперативная память»
"&f=185",   # Поиск в разделе «Мониторы. Проекторы.»
"&f=184"    # Поиск в разделе «SSD. HDD. USB Flash. Карты памяти»


]