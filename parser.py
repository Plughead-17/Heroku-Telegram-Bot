import json

import misc
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

##########################################################################
#
def clear_str(st):
    for item in misc.bad_symbols:
        st = st.replace(item, '')
    return st
