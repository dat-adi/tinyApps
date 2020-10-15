#!/usr/bin/python
# -*- coding: utf-8 -*-

# Front end window
import tkinter as tk
from tkinter import filedialog

# System and File access
import os

"""
oneSpotApp.py is a simple one click service that allows you to deploy all
the applications that you wish to, through a one time setup process.
"""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


def apps_in_file():
    if os.path.isfile("save.txt"):
        with open("save.txt", "r") as f:
            tempApps = f.read()
            tempApps = tempApps.split(",")
            apps = [x for x in tempApps if x.strip()]
    return apps


class mainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("One Spot App")

        # returns the app locations present in the file
        self.apps = apps_in_file()

        canvas = tk.Frame(self, height=700, width=700, bg="#DC143C")
        canvas.pack(side="top", fill="both", expand=True)

        frame = tk.Frame(self, bg="white")
        frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        openFile = tk.Button(
            self,
            text="Open File",
            padx=10,
            pady=5,
            fg="white",
            bg="#DC143C",
            command=self.add_apps,
        )
        openFile.pack()

        runApps = tk.Button(
            self,
            text="Run Apps",
            padx=10,
            pady=5,
            fg="white",
            bg="#DC143C",
            command=self.run_apps,
        )
        runApps.pack()

        for app in self.apps:
            label = tk.Label(frame, text=app)
            label.pack()

    def add_apps(self):
        filename = filedialog.askopenfilename(
            initialdir="/",
            title="Select App to add",
            filetypes=((".exe files", "*.exe"), ("All files", "*.*")),
        )
        self.apps.append(filename)

    def run_apps(self):
        for element in self.apps:
            os.startfile(element)

    def write_to_file(self):
        with open("save.txt", "a") as f:
            for element in self.apps:
                f.write(element + ",")


if __name__ == "__main__":
    App = mainApp()
    App.mainloop()
    App.write_to_file()
