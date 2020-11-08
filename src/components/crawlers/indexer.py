import requests
from bs4 import BeautifulSoup


def get_chapter_links():
    page = requests.get("https://wanderinginn.com/table-of-contents/").text
    soup = BeautifulSoup(page, "html.parser")
    contents_tag = soup.find("div", "entry-content")
    chapter_links = [link.get("href") for link in contents_tag.find_all("a")]

    no_slash_links = []
    double_slash_links = []

    for link in chapter_links:
        if link[-1] != "/":
            no_slash_links.append(chapter_links.index(link))
        if link[-2:] == "//":
            double_slash_links.append(chapter_links.index(link))

    for indice in no_slash_links:
        chapter_links[indice] = chapter_links[indice] + "/"

    for indice in double_slash_links:
        chapter_links[indice] = chapter_links[indice][:-1]

    return chapter_links


def set_chapter_file_links(chapter_links):
    with open("toc.txt", "w+") as f:
        f.write(str(chapter_links))
        f.close()


if __name__ == "__main__":
    set_chapter_file_links(get_chapter_links())
