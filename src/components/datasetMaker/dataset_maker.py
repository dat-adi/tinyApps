#!/usr/bin/python
# -*- coding: utf-8 -*-

# Directory traversing imports
from os import listdir
from os.path import getsize, splitext

# CSV file making
from csv import DictWriter

"""DSMkr is a simple folder traversing tool
 which identifies the files present in the folder
 and builds a CSV file to store the information in."""

# Owned
__author__ = "Datta Adithya"
__credits__ = ["Datta Adithya"]
__license__ = "MIT"
__maintainer__ = "Datta Adithya"
__email__ = "dat.adithya@gmail.com"


class mainApp:
    def __init__(self):
        self.dir_path = input("Enter the path to the directory: ")
        output_path = input("Enter the path to extract the csv to: ")
        csv_file_name = (
            input("Enter the name of the csv file( without extension ): ") + ".csv"
        )
        print("Indexing...")
        print("Folder: ", self.dir_path)
        print("Output Path: ", output_path)
        print("File Name: ", csv_file_name)
        self.file_indexer(output_path + "\\" + csv_file_name)

    def file_indexer(self, output_path_and_name):
        with open(output_path_and_name, "w", newline="") as f:
            fieldnames = ["File Name", "Extension", "File Type", "Size", "Path"]
            wtr = DictWriter(f, fieldnames=fieldnames)
            wtr.writerow(
                {
                    "File Name": "File Name",
                    "Extension": "Extension",
                    "File Type": "File Type",
                    "Size": "Size",
                    "Path": "Path",
                }
            )

            image_extension_list = [".jpg", ".png", ".svg"]
            text_extension_list = [".txt", ".md", ".html"]
            style_extension_list = [".css", ".scss"]
            code_extension_list = [".py", ".java", ".c", ".cpp", ".js"]
            media_extension_list = [".mp3", ".mp4"]
            application_extension_list = [".exe"]

            for one_file in listdir(self.dir_path):

                directories_in_folder = []

                file_name = self.dir_path + "\\" + one_file
                if splitext(file_name)[1] in image_extension_list:
                    file_type = "image"
                elif splitext(file_name)[1] in text_extension_list:
                    file_type = "text"
                elif splitext(file_name)[1] in style_extension_list:
                    file_type = "style"
                elif splitext(file_name)[1] in code_extension_list:
                    file_type = "programming"
                elif splitext(file_name)[1] in media_extension_list:
                    file_type = "media"
                elif splitext(file_name)[1] in application_extension_list:
                    file_type = "application"
                else:
                    file_type = "unknown"

                if getsize(file_name) != 0:
                    wtr.writerow(
                        {
                            "File Name": one_file[: one_file.rfind(".")],
                            "Extension": splitext(file_name)[1],
                            "File Type": file_type,
                            "Size": getsize(file_name),
                            "Path": file_name,
                        }
                    )
                else:
                    directories_in_folder.append(one_file)
        print("Directories present in the folder are : ", directories_in_folder)


# Main
if __name__ == "__main__":
    App = mainApp()
