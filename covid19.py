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
    content = "%04d/%02d/%02d %02d:%02d:%02d" % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec) + '\n' + covid19InfoDays()
    Github(access_token).get_user().get_repo(repository_name).create_issue(title='covid19', body=content)
