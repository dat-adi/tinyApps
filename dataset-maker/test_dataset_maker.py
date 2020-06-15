from os import listdir
from os.path import getsize, splitext
from csv import writer, DictWriter


def file_indexer(dir_path):
    with open('temp.csv', 'w', newline='') as f:
        fieldnames=["File Name", "Extension", "Size", "Path"]
        wtr = DictWriter(f, fieldnames=fieldnames)
        wtr.writerow(
            {
                "File Name": "File Name",
                "Extension": "Extension",
                "Size": "Size",
                "Path": "Path"
            }
        )
        for one_file in listdir(dir_path):
            file_name = dir_path + '\\' + one_file
            wtr.writerow(
                {
                    "File Name" : one_file[:one_file.rfind('.')],
                    "Extension" : splitext(file_name)[1],
                    "Size" : getsize(file_name),
                    "Path" : file_name
                }
            )


if __name__ == "__main__":
    directory_path = input("Enter the path to the directory: ")
    print("Indexing...")
    print("Folder: ", directory_path)
    file_indexer(directory_path)