import requests
import misc

######################################
#   Библиотека сетевого взаимодействия
#   - обработка статус кодов
#   - временные паузы и таймауты
#   - ищё чтонибуть...


##########################################################################
#       Получить старницу с сайта
def get_html(url, params = None):   # Запрос на сайт
    return requests.get(url, headers = misc.HEADERS, params = params)

##########################################################################
#       Проаерить статус коды
def get_page_confirm(url):   # Запрос на сайт
    page = get_html(url)
    if page.status_code == 404:
        print(url + " - bad url! - status code 404")
        return 0
    return page
