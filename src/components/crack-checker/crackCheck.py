#!/usr/bin/python
# -*- coding: utf-8 -*-

"""crackCheck is a application that is dedicated to checking whether or not the game is available cracked in real time, so long as you updated it."""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya", "Vijay Balaji"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


def Crack_checker(title):
    file = open("./assets/Data.txt", "r")
    data = file.read()
    if data.find(title) != -1:
        return True
    else:
        return False


if __name__ == "__main__":
    game = input(str("Enter the name of the game you want to check for : "))

    if Crack_checker(game):
        print("Game is Cracked")
    else:
        print("Game is not Cracked")

    input("Press any key to exit ")
