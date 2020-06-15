import os

temp_file = "D:\\tinyApps"
print(os.listdir(temp_file))
for one_file in os.listdir(temp_file):
    file_name = temp_file + '\\' + one_file
    if os.path.getsize(file_name) != 0:
        print(
            one_file,
            os.path.getsize(file_name),
            os.path.splitext(file_name)[1]
        )