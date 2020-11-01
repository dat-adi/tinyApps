import requests
from bs4 import BeautifulSoup
import os


def download(link, file_name):
    page = requests.get(link).text
    file = open(file_name, "w", encoding="utf-8")
    file.write(page)
    file.close()


def clean(file_name_in):
    raw = open(file_name_in, "r", encoding="utf-8")
    soup = BeautifulSoup(raw, "html.parser")
    raw.close()
    chapter_tag = soup.find('article', 'post')
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
    f = open(chapter_title + ".xhtml", "w", encoding="utf-8")
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
    f.close()
    os.remove(file_name_in)