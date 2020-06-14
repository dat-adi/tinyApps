from os import listdir
from csv import writer


def file_indexer(dir_path):
    print(listdir(dir_path))
    with open('temp.csv', 'w', newline='') as f:
        wtr = writer(f)
        wtr.writerow(listdir(dir_path))


if __name__ == "__main__":
    directory_path = input("Enter the path to the directory: ")
    print("Indexing...")
    print("Folder: ", directory_path)
    file_indexer(directory_path)