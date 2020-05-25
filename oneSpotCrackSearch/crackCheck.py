import requests
import json
import urllib

url = "https://api.crackwatch.com/api/games?&is_cracked=true&page=1"

def Crack_checker(link,title):
    url = urllib.request.urlopen(link)
    data = json.loads(url.read())
    strdata = str(data)
    if (strdata.find(title) != -1):
        print("Game is cracked")
    else:
        print("Game is not cracked")
    
Crack_checker(url,"Spirit of the North")
