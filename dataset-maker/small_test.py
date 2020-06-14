import os

temp_file = "D:\\tinyApps\\oneSpotCrackSearch"
print(os.listdir(temp_file))
for one_file in os.listdir(temp_file):
    print(one_file)
    file_name = temp_file + '\\' + one_file
    print(os.path.getsize(file_name))
    print(os.path.splitext(file_name)[1])