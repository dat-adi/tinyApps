import requests
from bs4 import BeautifulSoup
import json

def web(WebUrl):
    url = WebUrl
    code = requests.get(url)
    plain = code.text
    soup = BeautifulSoup(plain, "html.parser")
    tag = soup.find('div', 'entry-content').b


    chapter_tag = soup.find('article', 'post')
    chapter_test_tag = soup.find('div', 'entry-content')
    print(chapter_test_tag)
    with open('chapter.txt', "w", encoding="utf-8") as f:
        text = chapter_tag.get_text()
        text = text.replace("Previous Chapter", "").replace("Next Chapter", "")
        text = text.lstrip().rstrip()
        chapter_title = text.split('\n', 1)[0]
        text = text.replace(chapter_title, "")
        text = text.lstrip().rstrip()
        authored = text.split('\n', 1)[0]
        text = text.replace(authored, "")
        foot = "This entry was posted in Writing and tagged fantasy, inn, web novel, web serial, Writing by pirateaba. Bookmark the permalink."
        text = text.replace(foot, "")
        text = text.lstrip().rstrip()
        text = text.replace("\n", "</p>\n<p>")
        f.write('<html xmlns="http://www.w3.org/1999/xhtml">')
        f.write("\n<head>")
        f.write("\n<title>" + chapter_title + "</title>")
        f.write("\n</head>")
        f.write("\n<body>")
        f.write("\n<strong>" + chapter_title + "</strong>" + "\n<p>")
        f.write(text)
        f.write("</p>")
        f.write("\n</body>")
        f.write("\n</html>")
    
    with open('chapter.json', "w") as jsf:
        for line in chapter_tag.children:
            json.dumps(line.string)
        #for line in lines:
            #line = str(line)[3:-4]
            #print(line)


if __name__ == "__main__":
    web("https://wanderinginn.com/2016/07/27/1-01/")
