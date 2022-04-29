import requests
from bs4 import BeautifulSoup as Soup

def IOSDeveloperNewsScraping():
    soup = Soup(requests.get('https://developer.apple.com/kr/news').text, 'html.parser')
    # 해당 주소의 html 파일을 text로 불러옴
    href = soup.find('a', {'class': 'article-title'})
    # 최상위 게시물 주소 가져오기
    try:
        soup = Soup(requests.get('https://developer.apple.com' + href.attrs['href']).text, 'html.parser')
        # 게시물을 가져옴
    except:
        return "Soup Error: can't load article"
    content = "### " + href.text + "  \n"
    content += "###### " + soup.find('p', {'class': 'article-date'}).text + "  \n"
    origin_contents = soup.find('span', {'class': 'article-text'}).findChildren()
    mode = 0
    for con in origin_contents:
        if str(con)[:4] == "<ul>":
            mode = -1
        elif str(con)[:4] == "<ol>":
            mode = +1
        else:
            if str(con)[:4] == '<li>':
                content += (("* " if mode == -1 else str(mode)) + con.text + '  \n')
            elif str(con)[:3] != '<a ':
                content += (con.text + '  \n')
    return content
