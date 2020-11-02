import components
import zipfile
from indexer import get_chapter_links

def web(WebUrl):
    info = {
        "ChapterName": "TWI : ",
        "NovelName": "Wandering Inn",
        "author": "pirateaba"
    }

    link_list = get_chapter_links()
    file_list = []
    for x in range(len(link_list)):
        namer = x[36:-1]
        components.download(link_list[x], str(x) + ".html")
        components.clean(str(x) + ".html", info["ChapterName"] + str(namer) + ".xhtml")
        file_list.append(info["ChapterName"] + str(namer) + ".xhtml")
    components.generate(file_list, info["NovelName"], info["author"])


if __name__ == "__main__":
