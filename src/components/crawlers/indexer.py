import requests
from bs4 import BeautifulSoup

def get_chapter_links():
    page = requests.get("https://wanderinginn.com/table-of-contents/").text
    soup = BeautifulSoup(page, "html.parser")
    contents_tag = soup.find('div', 'entry-content')
    chapter_links = [link.get('href') for link in contents_tag.find_all('a')]

    return chapter_links


if __name__ == "__main__":
    print(get_chapter_links())