from os import listdir
from os.path import getsize, splitext
from csv import writer, DictWriter


def file_indexer(dir_path):
    with open('temp.csv', 'w', newline='') as f:
        fieldnames=["File Name", "Extension", "File Type", "Size", "Path"]
        wtr = DictWriter(f, fieldnames=fieldnames)
        wtr.writerow(
            {
                "File Name": "File Name",
                "Extension": "Extension",
                "File Type": "File Type",
                "Size": "Size",
                "Path": "Path"
            }
        )

        image_extension_list = ['.jpg', '.png', '.svg']
        text_extension_list = ['.txt', '.md', '.html']
        style_extension_list = ['.css', '.scss']
        code_extension_list = ['.py', '.java', '.c', '.cpp', '.js']

        for one_file in listdir(dir_path):

            directories_in_folder = []

            file_name = dir_path + '\\' + one_file
            if splitext(file_name)[1] in image_extension_list:
                file_type = 'image'
            elif splitext(file_name)[1] in text_extension_list:
                file_type = 'text'
            elif splitext(file_name)[1] in style_extension_list:
                file_type = 'style'
            elif splitext(file_name)[1] in code_extension_list:
                file_type = 'programming'

            if getsize(file_name) != 0:
                wtr.writerow(
                    {
                        "File Name" : one_file[:one_file.rfind('.')],
                        "Extension" : splitext(file_name)[1],
                        "File Type" : file_type,
                        "Size" : getsize(file_name),
                        "Path" : file_name
                    }
                )
            else:
                directories_in_folder.append(one_file)
    print("Directories present in the folder are : ", directories_in_folder)


if __name__ == "__main__":
    directory_path = input("Enter the path to the directory: ")
    print("Indexing...")
    print("Folder: ", directory_path)
    file_indexer(directory_path)