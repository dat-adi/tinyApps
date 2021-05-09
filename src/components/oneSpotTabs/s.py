import webbrowser as webb
import os
import pickle
import argparse

try:
    op = webb.get("firefox")
    url_and_name = {}
except:
    print("Looks like there's a browser issue")

if os.path.isfile("options"):
    temp_nu = open("options", "rb")
    url_and_name = pickle.load(temp_nu)

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--search", help="Name of the shortcut")
args = vars(ap.parse_args())

if args.get("search", False):
    op.open(url_and_name[args["search"].lower()])
else:
    print("1. Add website\n2. Remove website\n3. Select")
    option_pick = eval(input("> "))

    if option_pick == 1:
        name = input("Enter name : ")
        url = input("Enter url : ")
        url_and_name[name] = url
    elif option_pick == 2:
        print("Enter the name of the website to remove : ")
        removal_name = input("> ")
        del url_and_name[removal_name]
    elif option_pick == 3:
        for name, url in url_and_name.items():
            print(name.ljust(20, " "), url)
        temp_name = input("> ")
        op.open(url_and_name[temp_name.lower()])

    pickle.dump(url_and_name, open("options", "wb"))
