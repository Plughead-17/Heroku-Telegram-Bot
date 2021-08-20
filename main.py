import bot
import misc
import network
bad_symbols = "!@<>|\?"

def Test():
#    page = network.get_page_confirm(misc.URL)
#    items = parser.get_content(page)
    bot.sendmessagebot(str(items))


##########################################################################
#       Main
def main():

    print("RUN APP!")

    items = bot.getmessagebot()
    print(items)


    bot.RunRunFastUCan()

##########################################################################
if __name__ == "__main__":
    main() # - action