def Crack_checker(title):
    file = open("oneSpotCrackSearch/assets/Data.txt","r")
    data = file.read()
    if (data.find(title) != -1):
        return True
    else:
        return False

game = input(str("Enter the name of the game you want to check for : "))
if(Crack_checker(game)):
    print("Game is Cracked")
else:
    print("Game is not Cracked")

input("Press any key to exit ")