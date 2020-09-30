#!/usr/bin/python
# -*- coding: utf-8 -*-

# Front end window, and webbrowser deployment
import webbrowser as webb
import tkinter as tk

# System Access
import os
import pickle

""" OneSpotTabs is a simple one click mechanism in order to launch all of the webpages that you wish to, with a single click."""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"
# Function to add the urls into the file for later deployment.
def addUrl():
    for widget in frame.winfo_children():
        widget.destroy()

    name = input("Enter the name of the website : ")
    url = input("Enter the url of the website : ")
    url_and_name[name] = url
    print(name, "\t", url)
    for name, url in url_and_name.items():
        label = tk.Label(frame, text=(name, url), bg="#90AFC5")
        label.pack()

# Function to deploy all the urls stored in the file
def runUrl():
    for name, url in url_and_name.items():
        print(name, "\t", url)
        op.open(url, new=0)

# Function to delete the urls inserted into the file
def delUrl():
    to_delete = input("Enter the name of the website to delete : ")
    del url_and_name[to_delete]

# Main
if __name__ == "__main__":
    op = webb.get('opera')
    url_and_name = {}

    if os.path.isfile("tabs"):
        temp_nu = open('tabs', 'rb')
        url_and_name = pickle.load(temp_nu)

    root = tk.Tk()

    canvas = tk.Canvas(root, height=200, width=700, bg="#336B87")
    canvas.pack()

    frame = tk.Frame(canvas, bg="#2A3132")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    top_bar = tk.Label(root, text="oneSpotTabs", bg="#2A3132", fg="White")
    top_bar.pack(fill=tk.X)

    urlInput = tk.Button(root, text="Add Website", padx=10, pady=5, command=addUrl)
    urlInput.pack(side=tk.RIGHT)

    urlExecute = tk.Button(root, text="Run links", padx=10, pady=5, command=runUrl)
    urlExecute.pack(side=tk.RIGHT)

    urlDelete = tk.Button(root, text="Delete link", padx=10, pady=5, command=delUrl)
    urlDelete.pack(side=tk.RIGHT)

    root.mainloop()

    pickle.dump(url_and_name, open('tabs', 'wb'))