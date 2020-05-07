from bs4 import BeautifulSoup
import requests

ln_name = input("Enter the name of the light novel : ")
ln_name = ln_name.replace(' ', '-')
url = "https://m.wuxiaworld.co/" + ln_name + "/"

r = requests.get(url)
page_source = r.text

soup = BeautifulSoup(page_source, 'html.parser')
print(soup.text)
