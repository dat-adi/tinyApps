from urllib.request import urlopen
from json import loads
from datetime import datetime
from time import sleep

def last_time_check():
    date = open("./assets/LastUpdatedOn.txt","r")
    DateAndTime = date.read()
    if(len(DateAndTime)!=0):
        print("Last Updated On " + DateAndTime)
    date.close()

def last_page_check():
    page = open("./assets/LastPage.txt","r")
    pageNo = page.read()
    if(len(pageNo)!=0):
        startAt = int(pageNo) + 1
    else:
        startAt = 0
    page.close()
    return startAt

def last_time_update():
    date = open("assets/LastUpdatedOn.txt","w")
    now = datetime.now()
    DateAndTime = now.strftime("%d/%m/%Y %H:%M:%S")
    date.write(DateAndTime)
    date.close()

def last_page_update(lastUpdatedTill):
    page = open("assets/LastPage.txt","w")
    lastUpdatedTill = str(lastUpdatedTill)
    page.write(lastUpdatedTill)
    page.close()

def update(link):
    try:
        url = urlopen(link)
        data = loads(url.read())
        strdata = str(data)
        path = "assets/Data.txt"
        with open(path,"a",encoding="utf-8") as f:
            f.write(strdata)
        f.close()
    except:
        print("API RESPONSE ERROR...\nTry again in a while. We will continue from the page we left off.")
        input("Press any key to exit ")
        return False

if __name__ == "__main__":

    last_time_check()
    startAt = last_page_check()

    print("Update Process Started...\nThis might take a while. We will notify you once it is done.")
    lastUpdatedTill = 0
    for i in range(startAt,600):
        i = str(i)
        url = ("https://api.crackwatch.com/api/games?&is_cracked=true&page="+i)
        if update(url) is False:
            break
        print("Page " + i + " has been added")
        lastUpdatedTill = i

    print("Data has been successfully updated!")

    last_page_update(lastUpdatedTill)
    last_time_update()
    print('-' * 10)
    input("The data retrieved has been stored in Data.txt, press any key to safely exit.")
