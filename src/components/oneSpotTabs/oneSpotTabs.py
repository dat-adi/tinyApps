#!/usr/bin/python
# -*- coding: utf-8 -*-

# Front end window, and web browser deployment
import webbrowser as webb
import tkinter as tk

# System Access
import os
import pickle

""" OneSpotTabs is a simple one click mechanism in order to launch all of the web pages 
that you wish to, with a single click."""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


class mainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("One Spot Tabs")

        self.op = webb.get("opera")
        self.url_and_name = {}

        if os.path.isfile("tabs"):
            temp_nu = open("tabs", "rb")
            self.url_and_name = pickle.load(temp_nu)

        canvas = tk.Canvas(self, height=200, width=700, bg="#336B87")
        canvas.pack()

        self.frame = tk.Frame(canvas, bg="#2A3132")
        self.frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        top_bar = tk.Label(self, text="oneSpotTabs", bg="#2A3132", fg="White")
        top_bar.pack(fill=tk.X)

        urlInput = tk.Button(
            self, text="Add Website", padx=10, pady=5, command=self.add_url
        )
        urlInput.pack(side=tk.RIGHT)

        urlExecute = tk.Button(
            self, text="Run links", padx=10, pady=5, command=self.run_url
        )
        urlExecute.pack(side=tk.RIGHT)

        urlDelete = tk.Button(
            self, text="Delete link", padx=10, pady=5, command=self.del_url
        )
        urlDelete.pack(side=tk.RIGHT)

        for name, url in self.url_and_name.items():
            label = tk.Label(self.frame, text=(name, url), bg="#90AFC5")
            label.pack()

    def add_url(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        name = input("Enter the name of the website : ")
        url = input("Enter the url of the website : ")
        self.url_and_name[name] = url
        print(name, "\t", url)
        for name, url in self.url_and_name.items():
            label = tk.Label(self.frame, text=(name, url), bg="#90AFC5")
            label.pack()

    def run_url(self):
        for name, url in self.url_and_name.items():
            print(name, "\t", url)
            self.op.open(url, new=0)

    def del_url(self):
        to_delete = input("Enter the name of the website to delete : ")
        del self.url_and_name[to_delete]

    def write_to_file(self):
        pickle.dump(self.url_and_name, open("tabs", "wb"))


if __name__ == "__main__":
    App = mainApp()
    App.mainloop()
    App.write_to_file()
