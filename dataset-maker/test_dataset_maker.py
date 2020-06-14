from os import listdir
from os.path import getsize, splitext
from csv import writer, DictWriter


def file_indexer(dir_path):
    print(listdir(dir_path))
    with open('temp.csv', 'w', newline='') as f:
        fieldnames=["File Name", "Extension", "Size"]
        wtr = DictWriter(f, fieldnames=fieldnames)
        for one_file in listdir(dir_path):
            file_name = dir_path + '\\' + one_file
            wtr.writerow({"File Name" : one_file, "Extension" : splitext(file_name)[1], "Size" : getsize(file_name)})


if __name__ == "__main__":
    directory_path = input("Enter the path to the directory: ")
    print("Indexing...")
    print("Folder: ", directory_path)
    file_indexer(directory_path)