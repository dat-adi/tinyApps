from json import loads
from urllib.request import urlopen
from sys import exit as Exit

def Crack_checker(link,title):
    try:
        url = urlopen(link)
        data = loads(url.read())
        strdata = str(data)
        if(strdata!="[]"):
            if (strdata.find(title) != -1):
                return True
            else:
                return False
        else:
            print("Game is not cracked")
            input("Enter any key to exit ")
            Exit(0)
    except:
        print("Connection error.")
        input("Press any key to exit")
        Exit(0)

game = input(str("Enter the name of the game you want to check for : "))
number_of_pages = int(input("How many pages do you want to search?\n"))
for i in range(number_of_pages):
    print("searching...")
    if(i >= 50 and i%50):
        print("In page {}, will continue searching...".format(i))
    i = str(i)
    url = ("https://api.crackwatch.com/api/games?&is_cracked=true&page="+i)
    if(Crack_checker(url,game)):
        print("Game is Cracked")
        break
input("Press any key to exit ")
