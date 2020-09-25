#!/usr/bin/python
# -*- coding: utf-8 -*-

# Front end window
import tkinter as tk
from tkinter import filedialog, Text

# System and File access
import os
import pickle

"""oneSpotApp.py is a simple one click service that allows you to deploy all the applications that you wish to, through a one time setup process."""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


    

class oneSpotApp:
    def __init__(self):
        self.apps = []
        file_read()
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, height=700, width=700, bg="#DC143C").pack()
        self.frame = tk.Frame(self.root, bg="white").place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        self.openFile = tk.Button(self.root, text="Open File", padx=10, pady=5, fg="white", bg="#DC143C", command=addApps).pack()
        self.runApps = tk.Button(self.root, text="Run Apps", padx=10, pady=5, fg="white", bg="#DC143C", command=runApps).pack()
    
        for app in apps:
            label = tk.Label(self.frame, text=app).pack()
    
    def file_read(self):
        if os.path.isfile('save.txt'):
            with open('save.txt', 'r') as f:
                tempApps = f.read()
                tempApps = tempApps.split(',')
                self.apps = [x for x in tempApps if x.strip()]
    
    def file_write(self):
        with open('save.txt', 'w') as f:
            for app in self.apps:
                f.write(app + ',')

    # function to add the apps into the file
    def addApps(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        filename = filedialog.askopenfilename(initialdir="/", title="Select App to add",
            filetypes=(('.exe files', "*.exe"), ("All files", "*.*"))
        )

        self.apps.append(filename)
        print(filename)
        for app in self.apps:
            label = tk.Label(frame, text=app, bg="gray").pack()

    # function to deploy all the apps through the file locations provided.
    def run_apps(self):
        for app in self.apps:
            os.startfile(app)

# main
if __name__ == "__main__":
    apps = []


    root = tk.Tk()

    canvas = tk.Canvas(root, height=700, width=700, bg="#DC143C")
    canvas.pack()

    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#DC143C", command=addApps)
    openFile.pack()

    runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#DC143C", command=runApps)
    runApps.pack()

    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()

    root.mainloop()

    with open('save.txt', 'w') as f:
        for app in apps:
            f.write(app + ',')