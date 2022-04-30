import os
import requests
from bs4 import BeautifulSoup as Soup
from datetime import datetime, timedelta
from github import Github



def covid19InfoDays():
    soup = Soup(requests.get(
        'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=covid').text,
                'html.parser')
    info = soup.find('div', {'class': 'status_info'})
    content = info.text + "\n"
    return content


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    # token
    repository_name = "Jeonhui"
    # repository name
    
    yesterday = str(date.today() - timedelta(days=1)) # 현재 날짜의 하루 전
    title = "[ %s년 %s월 %s일" %(yesterday[:4], yesterday[5:7], yesterday[8:]) + ' 코로나 확진자 수 ]' # issue title
    body = covid19InfoDays() # body 크롤링 데이터
    
    Github(access_token).get_user().get_repo(repository_name).create_issue(title=title, body=body)
    # issue 생성
