import os
import requests
from bs4 import BeautifulSoup as Soup


def IOSDeveloperNewsScraping():
    soup = Soup(requests.get('https://developer.apple.com/kr/news/').text, 'html.parser')
    # 해당 주소의 html 파일을 text로 불러옴

    href = soup.find('a', {'class': 'article-title'})
    # 최상위 게시물 주소 가져오기

    try:
        soup = Soup(requests.get('https://developer.apple.com' + href.attrs['href']).text, 'html.parser')
        # 게시물을 가져옴
    except:
        return "Soup Error: can't load article"
        # 게시물 가져오기 실패

    section = soup.find('section', 'article-content-container')

    title = ""
    temp = section.find('img', 'article-image')
    if temp is not None:
        title = '![이미지](https://developer.apple.com'+temp.attrs['src']+')  \n'

    title += '###  '+section.find('h2','article-title').text + "  \n"
    date = "###### " + soup.find('p', 'article-date').text + "  \n"
    text = str(section.find('span', 'article-text'))
    return title + date + text


if __name__ == "__main__":
    bufsize = 1024
    f = open('./README.md', 'w')
    info = open('./info.md', 'r')
    for data in info.readlines():
        f.write(data)
    f.write(IOSDeveloperNewsScraping())
    f.close()
    info.close()
