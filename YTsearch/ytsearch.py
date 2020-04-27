import webbrowser as webb
import argparse

print("ytsearch 1.0.0 | tinyApps")

ap = argparse.ArgumentParser()
ap.add_argument('-s', '--search', help="Enter the search request") #takes the arguments 
args = vars(ap.parse_args()) #creates a dictionary for args to take the search request

if not args.get("search", False):
    search_query = input("SearchQuery> ")
else:
    search_query = args["search"]

search_query = search_query.replace(" ", "+") # replaces the spaces in the url
webb.open("https://www.youtube.com/results?search_query={}".format(search_query)) #searches for it in youtube