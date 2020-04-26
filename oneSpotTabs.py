import webbrowser as webb #module allows us to access the web browser
import tkinter as tk
import os

url_and_name = {}

root = tk.Tk()

def addUrl():
    name = input("Enter the name of the website : ")
    url = input("Enter the url of the website : ")
    url_and_name[name] = url
    label = tk.Label(frame, text=(name, "\t", url), bg="#90AFC5")
    label.pack()
    print(name, "\t", url)


def runUrl():
    for url in url_and_name.items():
        # can try to make the website go up by just typing name but, redundancy.
        webb.open(url, new=0)

canvas = tk.Canvas(root, height=200, width=700, bg="#336B87")
canvas.pack()

frame = tk.Frame(canvas, bg="#2A3132")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

urlInput = tk.Button(root, text="Add Website", padx=10, pady=5, command=addUrl)
urlInput.pack()

urlExecute = tk.Button(root, text="Run links", padx=10, pady=5, command=runUrl)
urlExecute.pack()

root.mainloop()

with open("tabs.txt", 'w') as f:
    for name, url in url_and_name.items():
        f.write("{}:{},".format(name, url))