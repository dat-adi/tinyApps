import requests
import json
import urllib
import sys
import requests_cache

requests_cache.install_cache('cache')
def Crack_checker(link,title):
    try:
        url = urllib.request.urlopen(link)
    except:
        print("CONNECTION ERROR : 500 INTERNAL SERVER ERROR")
        input("Enter any key to exit ")
        sys.exit(0)
    data = json.loads(url.read())
    strdata = str(data)
    if(strdata!="[]"):
        if (strdata.find(title) != -1):
            return True
        else:
            return False
    else:
        print("Game is not cracked")
        input("Enter any key to exit ")
        sys.exit(0)

game = input(str("Enter the name of the game you want to check for : "))
for i in range(600):
    i = str(i)    
    url = ("https://api.crackwatch.com/api/games?&is_cracked=true&page="+i)
    if(Crack_checker(url,game)):
        print("Game is Cracked")
        break
input("Press any key to exit ")
