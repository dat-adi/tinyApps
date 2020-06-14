import csv
from os import listdir


def file_indexer(dir_path):
    print(listdir(dir_path))


if __name__ == "__main__":
    directory_path = input("Enter the path to the directory: ")
    print("Indexing...")
    print("Folder: ", directory_path)
    file_indexer(directory_path)