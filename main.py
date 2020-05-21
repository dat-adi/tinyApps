# Essentially a hub for all of the programs to be accessed through.
import oneSpotApp
import oneSpotTabs
import YTsearch
import os

def help_user():
    print(
'''
The point of having oneSpotApps together is to simply launch them all faster instead of typing it all one by one.
As such, all you have to do is, follow the method to using the oneSpotApps with ease.

oneSpotApp
----------
apps
\tRuns oneSpotApp, opening up the interface.
tabs
\tRuns oneSpotTabs, with the interface opening up.
yts
\tRuns YTsearch.
'''
        )

def about():
    print(
'''
A simple one click interface to deploy apps, urls, and searches in particular websites.
tinyApps strives to deliver simple one line access to all these features in the shortest time possible.

oneSpotApps is simply a hub for deploying all your necessary applications to create your own workspace.
oneSpotTabs essentially keeps a records of the urls you need, if you wish to deploy all the websites for your workspace at once.
YTsearch queries your search on YouTube and brings you the results you need in your browser.

Developed by Dat Adi, tinyApps.
'''
        )

print(
    '''
tinyApps v1.0 | Hosted under MIT | May 18 2020
Type 'help' or 'about' for more info, and'quit' to exit
    '''
)

while True:
    used = input('> ')
    if used == 'help':
        help_user()
    elif used == 'about':
        about()
    elif used == 'apps':
        print("oneSpotApp/oneSpotApp.py")
    elif used == 'tabs':
        print("oneSpotTabs/oneSpotTabs.py")
    elif used == 'yts':
        print("YTsearch/ytsearch.py")
    elif used == 'quit':
        break
    else:
        print("invalid command")
        print('restarting...')
