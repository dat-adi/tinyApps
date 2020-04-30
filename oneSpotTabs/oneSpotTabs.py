import webbrowser as webb #module allows us to access the web browser
import tkinter as tk
import os
import pickle

op = webb.get('opera')
url_and_name = {}

if os.path.isfile("tabs"):
    temp_nu = open('tabs', 'rb')
    url_and_name = pickle.load(temp_nu)

root = tk.Tk()

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

def runUrl():
    for name, url in url_and_name.items():
        # can try to make the website go up by just typing the name but, redundancy.
        print(name, "\t", url)
        op.open(url, new=0)

def delUrl():
    to_delete = input("Enter the name of the website to delete : ")
    del url_and_name[to_delete]

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