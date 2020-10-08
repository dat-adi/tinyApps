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


class yts:
    def __init__(self):
        ap = ArgumentParser() 
        # ap.add_arguments take the arguments 
        ap.add_argument('-s', '--search', help="Enter the search request")
        args = vars(ap.parse_args()) #creates a dictionary for args to take the search request

        if not args.get("search", False):
            self.search_query = input("SearchQuery> ")
        else:
            self.search_query = args["search"]

    def run_search(self):
        self.search_query = self.search_query.replace(" ", "+") # replaces the spaces in the url
        wbopen("https://www.youtube.com/results?search_query={}".format(self.search_query)) #searches for it in youtube


# Main
if __name__ == "__main__":
    print("ytsearch 1.0.0 | tinyApps")
    test = yts()
    test.run_search()

