import components
import zipfile

def web(WebUrl):
    components.download(WebUrl, "chapter.txt")
    chapter_name = components.clean("chapter.txt")
    info = {
        "ChapterName": chapter_name,
        "NovelName": "Wandering Inn",
        "author": "pirateaba"
    }

    file_list = []
    components.generate(file_list, info["NovelName"], info["author"], starting_chapter, ending_chapter)


if __name__ == "__main__":
    web("https://wanderinginn.com/2016/07/27/1-01/")
