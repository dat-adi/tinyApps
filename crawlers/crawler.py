import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating project ' + directory)
        os.makedirs(directory)

# Creating the data files.
def create_data_files(project_name, base_url):
    queue = project_name + "/queue.txt"
    crawled = project_name + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# Entering data into write_file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()

#Adding data to an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + "\n")

#Delete the contents of the file
def delete_file_contents(path):
    with open(path, 'w'):
        pass

#Read a file and convert each file to set items
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as f:
        for line in f:
            results.add(line.replace('\n', ''))
    return results

#Iterating through a set, each item -> new line in file
def set_to_file(links, file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(link)


create_project_dir("crawler_test")
create_data_files('crawler_test', 'https://w.wuxiaworld.co/')

