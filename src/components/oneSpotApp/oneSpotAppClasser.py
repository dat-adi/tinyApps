#!/usr/bin/python
# -*- coding: utf-8 -*-

# Front end window
import tkinter as tk
from tkinter import filedialog, Text

# System and File access
import os
import pickle

"""oneSpotApp.py is a simple one click service that allows you to deploy all the applications that you wish to,
 through a one time setup process."""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


class mainApp(tk.Tk):
    def __init__(self, conn, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("One Spot App")
        
        canvas = tk.Frame(self, height=700, width=700, bg="#DC143C")
        canvas.pack(side="top", fill="both", expand=True)

