import requests
from bs4 import BeautifulSoup as Soup
import time
from github import Github
import os


def covid19InfoDays():
    soup = Soup(requests.get(
        'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=covid').text,
                'html.parser')
    info = soup.find('div', {'class': 'status_info'})
    content = info.text + "\n"
    return content


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "Jeonhui"
    now = time.localtime()
    body = covid19InfoDays()
    title = "%04d년 %02d월 %02d일" % (
        now.tm_year, now.tm_mon, now.tm_mday + 1) + ' 코로나 확진자 수'
    Github(access_token).get_user().get_repo(repository_name).create_issue(title=title, body=body)
