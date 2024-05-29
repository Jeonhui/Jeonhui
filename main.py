import requests
from bs4 import BeautifulSoup as Soup
import re


class MarkdownConverter:
    @staticmethod
    def image(name: str, src: str):
        if src is None: return ""
        return MarkdownConverter.br(f"![{name}]({src})")

    @staticmethod
    def image_tag(src: str, alt: str, width: int):
        if src is None: return ""
        return "\n" + MarkdownConverter.br(f"<img src=\"{src}\" alt=\"{alt}\" width=\"{width}\"/>")

    @staticmethod
    def h2(text: str):
        if text is None: return ""
        return "\n" + MarkdownConverter.br(f"## {text}")

    @staticmethod
    def p(text: str):
        if text is None: return ""
        return "\n" + MarkdownConverter.br(f"###### {text}")

    @staticmethod
    def br(text: str):
        if text is None: return ""
        return f"{text}  \n"


class Scrapper:
    soup = None
    select = None

    def __init__(self, domain=None, parser: str = 'html.parser'):
        if domain is not None:
            self.set_soup(domain, parser)

    def set_soup(self, domain: str, parser: str = 'html.parser'):
        self.soup = Soup(requests.get(domain).text, parser)

    def select_tag(self, tag: str, attrs=None):
        self.select = self.soup.find(tag, attrs)

    def _get_select(self):
        tag = self.soup
        if self.select is not None:
            tag = self.select
        return tag

    def _get_attr(self, tag: str, attrs, attr: str):
        if attrs is None:
            attrs = {}
        tag = self._get_select().find(tag, attrs)
        if tag is None: return tag
        return tag.attrs[attr]

    def get_tag_text(self, tag: str, attrs):
        tag = self._get_select().find(tag, attrs)
        if tag is None: return tag
        return tag.text

    def get_image_src(self, attrs=None):
        return self._get_attr('img', attrs, 'src')

    def get_a_href(self, attrs=None):
        return self._get_attr('a', attrs, 'href')

    def get_str(self, tag: str, attrs):
        return str(self._get_select().find(tag, attrs))


class iOSDevNewsScrapper:
    scrapper = Scrapper()

    def __init__(self):
        self.domain = 'https://developer.apple.com'

    def scrap(self):
        self.scrapper.set_soup(self.domain + '/news/')
        href = self.scrapper.get_a_href({'class': 'article-title'})
        self.scrapper.set_soup(self.domain + href)

        self.scrapper.select_tag('section', 'article-content-container')

        image_src = self.scrapper.get_image_src('article-image')
        image_src = ('https://developer.apple.com' +  image_src) if image_src is not None else None
        title = self.scrapper.get_tag_text('h2', 'article-title')
        date = self.scrapper.get_tag_text('p', 'article-date')
        content = self.scrapper.get_str('div', 'article-text')
        return image_src, title, date, content

    def convert(self, image_src, title, date, content):
        md_image = MarkdownConverter.image_tag(image_src, "news_image", 100)
        md_title = MarkdownConverter.h2(title)
        md_date = MarkdownConverter.p(date)
        md_content = MarkdownConverter.br(content)
        return "".join([md_image, md_title, md_date, md_content])

    def scrap_and_convert(self):
        try:
            image_src, title, date, content = self.scrap()
        except Exception as e:
            return str(e)
        return re.sub(" ", "", self.convert(image_src, title, date, content))


if __name__ == "__main__":
    ios_dev_news_scrapper = iOSDevNewsScrapper()
    with open('./README.md', 'w') as readme:
        with open('./info.md', 'r') as info:
            for line in info.readlines():
                readme.write(line)
        news = ios_dev_news_scrapper.scrap_and_convert()
        readme.write(news)
