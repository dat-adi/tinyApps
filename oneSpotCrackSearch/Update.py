from urllib.request import urlopen
from json import loads
from datetime import datetime
import time
import sys

def update(link):
    time.sleep(2)
    url = urlopen(link)
    data = loads(url.read())
    strdata = str(data)
    path = "oneSpotCrackSearch/assets/Data.txt"
    with open(path,"a",encoding="utf-8") as f:
        f.write(strdata)
    f.close()

print("Update Process Started...\nThis might take a while. We will notify you once it is done.")
for i in range(500):
    i = str(i)
    url = ("https://api.crackwatch.com/api/games?&is_cracked=true&page="+i)
    update(url)
    print("Page " + i + " has been added")

print("Data has been successfully updated!")

input("Press any key to exit ")
