# Essentially a hub for all of the programs to be accessed through.
print(
    '''
Naruita's tinyApps v1.0 | Hosted under MIT | May 18 2020
Type 'help' or 'about' for more info
    '''
)
while True:
    used = input('> ')
    if used == 'help':
        print(
'''
The point of having oneSpotApps together is to simply launch them all faster instead of typing it all one by one.
As such, all you have to do is, follow the method to using the oneSpotApps with ease.

oneSpotApp
----------
app
\tRuns oneSpotApp, opening up the interface.
tabs(...)
\tRuns oneSpotTabs, with ... signifying the url you wish to add.
yts(...)
\tRuns YTsearch, with ... signifying the name of the video you wish to search for.
'''
        )
    elif used == 'about':
        print(
'''
A simple one click interface to deploy apps, urls, and searches in particular websites.
Naruita's tinyApps strives to deliver simple one line access to all these features in the shortest time possible.
'''
        )
    else:
        break
