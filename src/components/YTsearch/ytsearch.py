#!/usr/bin/python
# -*- coding: utf-8 -*-

# Web browser deployment
from webbrowser import open as wbopen

# Argument parsing
from argparse import ArgumentParser

'''YTSearch is a simple searching tool which retrieves results from YouTube and presents them to you in a new web browser.'''
# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"

# Main
if __name__ == "__main__":
    print("ytsearch 1.0.0 | tinyApps")

    ap = ArgumentParser()
    ap.add_argument('-s', '--search', help="Enter the search request") #takes the arguments 
    args = vars(ap.parse_args()) #creates a dictionary for args to take the search request

    if not args.get("search", False):
        search_query = input("SearchQuery> ")
    else:
        search_query = args["search"]

    search_query = search_query.replace(" ", "+") # replaces the spaces in the url
    wbopen("https://www.youtube.com/results?search_query={}".format(search_query)) #searches for it in youtube