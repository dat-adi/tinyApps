import components
import zipfile

def web(WebUrl):
    components.download(WebUrl, "chapter.txt")
    components.clean("chapter.txt")


def generate(html_files, novelname, author, chapter_s, chapter_e):
    epuc = zipfile.ZipFile(novelname + "_" + chapter_s + "-" + chapter_e + ".epub", "w")
    

if __name__ == "__main__":
    web("https://wanderinginn.com/2016/07/27/1-01/")
