#!/usr/bin/python
# -*- coding: utf-8 -*-

# importing various different applications
from components import crackChecker, datasetMaker, oneSpotApp, oneSpotTabs, YTsearch


class Blueprint:
    @staticmethod
    def run():
        print("Here's a list of tinyApps that are ready to be run!")
        print("1. oneSpotApp")
        response = eval(input("> "))
        App = oneSpotApp.oneSpotApp.mainApp()
        App.mainloop()
