import os
import requests
from bs4 import BeautifulSoup as Soup


def iOSDeveloperNewsScraping():
    soup = Soup(requests.get('https://developer.apple.com/news/').text, 'html.parser')
    # 해당 주소의 html 파일을 text로 불러옴

    # 최상위 게시물 주소 가져오기
    href = soup.find('a', {'class': 'article-title'})

    try:
        # 게시물 가져오기
        soup = Soup(requests.get('https://developer.apple.com' + href.attrs['href']).text, 'html.parser')
    except:
        # 게시물 가져오기 실패
        return "Soup Error: can't load article"


    section = soup.find('section', 'article-content-container')

    title = ""
    temp = section.find('img', 'article-image')
    if temp is not None:
        title = '![news_image](https://developer.apple.com' + temp.attrs['src'] + ')  \n'

    title += '###  ' + section.find('h2', 'article-title').text + "  \n"
    date = "###### " + soup.find('p', 'article-date').text + "  \n"
    text = str(section.find(class_='article-text'))
    return title + date + text


if __name__ == "__main__":
    f = open('./README.md', 'w')
    info = open('./info.md', 'r')
    for data in info.readlines():
        f.write(data)
    f.write(iOSDeveloperNewsScraping())
    f.close()
    info.close()
