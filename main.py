import urllib.request
from bs4 import BeautifulSoup

def request_html():
    url = "https://www.gutenberg.org/browse/scores/top"
    html = urllib.request.urlopen(url).read()
    print(f'Hi, {html}')
    oup = BeautifulSoup(html, "html.parser")
    page_content = oup.find_all("div",{"class":"page_content"})
    result = page_content.pop().find_all("ol")
    for tag_ol in result:
        a_list = tag_ol.find_all('a')
        for tag_a in a_list:
            bookname = tag_a.text
            print(bookname)