import os

temp_file = "D:\\tinyApps\\oneSpotCrackSearch"
print(os.listdir(temp_file))
for one_file in os.listdir(temp_file):
    file_name = temp_file + '\\' + one_file
    print(one_file, os.path.getsize(file_name), os.path.splitext(file_name)[1])