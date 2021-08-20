#Tutorial https: // www.youtube.com / watch?v = wVSxrn5IBZo

# Импортируем библиотеки
import os
import sys
import telebot
import time
import logging
from bs4 import BeautifulSoup
import requests
# Импортируем токен бота и список каналов
from data import TOKEN, list

# Настраиваем логер
logging.basicConfig(filename="logfile.py", level=logging.INFO)
# Готовим бота к запуску
bot = telebot.TeleBot(TOKEN)


# Создаем клас из которогу будем собирать ссылки
class Kanal:
    name: str = list[0]
    stpage: int = list[1]
    embaded: str = "?embed=1"


# Создаем функционал отправки сообщения с проверкой ошибок
def solver(link):
    try:
        bot.send_message(chat_id=-100 ** ** ** ** ** *, text = link)
        logging.info('No problem detected')
    except OSError:
        logging.info("ConnectionError - Sending again after 5 seconds!!!")
        time.sleep(5)
        bot.send_message(chat_id=-100 ** ** ** ** ** *, text = link)
        logging.info('Problem solved')


# Создаем основную функции
def collector():
    logging.info("Collector started")
    # Обнуляем счетчики которые будут двигать нас по списку каналов
    counter = 0
    counter2 = 1
    Kanal.name = list[counter]
    Kanal.stpage = list[counter2]
    # Запускаем обход каналов
    while True:
        # Выводим в консоль кота и имя канала который проверяеться
        clear = lambda: os.system('cls')
        clear()
        print()
        print("　　　　　 ／＞　 フ")
        print("　　　　　| 　0 0 |")
        print("　 　　　／`ミ _x 彡")
        print("　　 　 /　　　 　 |")
        print("　　　 /　 ヽ　　 ﾉ")
        print("　／￣|　　 |　|　|")
        print("　| (￣ヽ＿_ヽ_)_)")
        print("　＼二つ")
        print("Проверяем канал ", Kanal.name)
        time.sleep(2)
        clear = lambda: os.system('cls')
        clear()
        print()
        print("　　　　　 |＞　 フ ")
        print("　　　　　|  0 0  |")
        print("　 　　　／ミ x_ 彡")
        print("　　 　 /　　　 　 |")
        print("　　　 /　 ヽ　　 ﾉ")
        print("　／￣|　　 |　|　|")
        print("　| (￣ヽ＿_ヽ_)_)")
        print("　＼二つ")
        print("Проверяем канал ", Kanal.name)
        time.sleep(2)
        # Собираем ссылку
        r = requests.get(Kanal.name + str(Kanal.stpage) + Kanal.embaded)
        # Запускаем суп
        data = r.text
    soup = BeautifulSoup(data, 'lxml')
    # Проверяем есть ли новость по ссылке
    pg_not_fnd = soup.find_all("div", {"class": "tgme_widget_message_error"})
    if len(pg_not_fnd) > 0:
        # Если новости нет то увеличиваем счетчики и обноляем ссылку
        counter = counter + 2
        counter2 = counter2 + 2
        # Считаем максимальную длину нашего списка
        stop = len(list)
        # Ориентируясь по максимальной длинне списка останавливаем поиск
        if counter >= stop:
            logging.info("Sleeping")
            # Выводим кота и счетчик времени с паузой примерно в 15 минут
            for i in reversed(range(1, 500)):
                time.sleep(1)
                clear = lambda: os.system('cls')
                clear()
                print()
                print("　　　　　 ／＞　 フ")
                print("　　　　　| 　_　 _|")
                print("　 　　　／`ミ _x 彡")
                print("　　 　 /　　　 　 |")
                print("　　　 /　 ヽ　　 ﾉ")
                print("　／￣|　　 |　|　|")
                print("　| (￣ヽ＿_ヽ_)_)")
                print("　＼二つ")
                print()
                sys.stderr.write(f"{i:2d}\r")
                time.sleep(1)

                time.sleep(1)
                clear = lambda: os.system('cls')
                clear()
                print()
                print("　　　　　 ／＞　 フ")
                print("　　　　　| 　_　 _|")
                print("　 　　　／`彡 _Х ミ")
                print("　　 　 /　　　 　 |")
                print("　　　 /　 ヽ　　 ﾉ")
                print("　／￣|　　 |　|　|")
                print("　| (￣ヽ＿_ヽ_)_)")
                print("　＼二つ")
                print()
                sys.stderr.write(f"{i:2d}\r")
                time.sleep(1)
            # Выходим из цикла While
            break
        Kanal.name = list[counter]
        Kanal.stpage = list[counter2]
    else:
        # Если новость найдена ищем списку
        for results in soup.find_all("a", {"class": "tgme_widget_message_date"}):
            link = results.get('href')
            # Увеличиваем номер новости в списке чтоб не брать одну и ту же новость заново
            list[counter2] = int(list[counter2]) + 1
            # Отправляем в solver
            solver(link)
            # открываем файл data и перезаписываем его
            output = open("data.py", 'w')
            # Так как файл полностью перезаписываться то сначало вносим наш токен
            print("TOKEN = '11**********9:AA*******************************'", file=output)
            # А потом обновленный список каналов
            print("list =", list, file=output)
            output.close()
        # Переходим к следующей страничке канала для поиска новости на ней
        Kanal.stpage = str(int(Kanal.stpage) + 1)


# Запускаем нашу основную функцию на бесконечную обработку
while True:
    logging.info("Reboot True")
    collector()

** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **

TOKEN = '11**********9:AA*******************************'
list = ['https://t.me/SecLabNews/', 7451, 'https://t.me/overlamer1/', 531, 'https://t.me/thehackernews/', 680,
        'https://t.me/haccking/', 4872, 'https://t.me/opennet_ru/', 4188, 'https://t.me/dataleak/', 1623,
        'https://t.me/Social_engineering/', 972, 'https://t.me/hack_a_day/', 39, 'https://t.me/tstmwschanell/', 36,
        'https://t.me/pystyle/', 36, 'https://t.me/exploitex/', 1338, 'https://t.me/alexmakus/', 3434,
        'https://t.me/xakep_ru/', 9049, 'https://t.me/webware/', 3009, 'https://t.me/parseronio/', 10000]