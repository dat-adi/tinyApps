from os import listdir
from os.path import getsize, splitext
from csv import writer, DictWriter


def file_indexer(dir_path):
    print(listdir(dir_path))
    with open('temp.csv', 'w', newline='') as f:
        wtr = DictWriter(f)
        for one_file in listdir(dir_path):
            print(one_file)
            file_name = dir_path + '\\' + one_file
            print(getsize(file_name))
            print(splitext(file_name)[1])
            wtr.writerow({"File Name" : file_name, "Extension" : splitext(file_name), "Size" : getsize(file_name)})


if __name__ == "__main__":
    directory_path = input("Enter the path to the directory: ")
    print("Indexing...")
    print("Folder: ", directory_path)
    file_indexer(directory_path)