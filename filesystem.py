import json
import misc

LOG_FILE = misc.LOG_FILE

##########################################################################
#           Логи в файл и принт
def msg(massage):
    with open(LOG_FILE, 'a') as file:
        file.write(str(massage) + '\n')
    print(massage)


##########################################################################
#
def jinfile(data, filename = "response.json"):
    with open(filename, 'w', encoding = "utf-16") as file:
        json.dump(data, file, indent = 2, ensure_ascii = False)


def LoadspaceTrack():

    fileName = "search_data.dat"
    i =123
    with open(file=fileName, mode='wb+') as file:
        file.write("123")
