import os
from scraping import IOSDeveloperNewsScraping

if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    f = open('./README.md', 'w')
    f.write(IOSDeveloperNewsScraping())
    f.close()
