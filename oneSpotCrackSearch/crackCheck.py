import requests
import json
import urllib
from time import sleep
import sys

def Crack_checker(link,title):
    url = urllib.request.urlopen(link)
    data = json.loads(url.read())
    strdata = str(data)
    if(strdata!="[]"):
        if (strdata.find(title) != -1):
            return True
        else:
            return False
    else:
        print("Game is not cracked")
        sleep(20)
        sys.exit(0)

game = input(str("Enter the name of the game you want to check for : "))
for i in range(600):
    i = str(i)    
    url = ("https://api.crackwatch.com/api/games?&is_cracked=true&page="+i)
    if(Crack_checker(url,game)):
        print("Game is Cracked")
        break
