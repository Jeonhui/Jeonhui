import re
from email.utils import parsedate_to_datetime

import requests
import feedparser


class MarkdownConverter:
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


class iOSDevNewsRSS:
    FEED_URL = 'https://developer.apple.com/news/rss/news.rss'

    def fetch_latest(self):
        response = requests.get(self.FEED_URL)
        feed = feedparser.parse(response.text)
        if not feed.entries:
            return None
        return feed.entries[0]

    @staticmethod
    def _format_date(date_str):
        try:
            dt = parsedate_to_datetime(date_str)
            return dt.strftime('%B %d, %Y')
        except Exception:
            return date_str

    @staticmethod
    def _clean_html(html):
        # Remove inline-article-image div (image is shown separately)
        html = re.sub(r'<div class="inline-article-image">.*?</div>', '', html, flags=re.DOTALL)
        # Remove icon spans, keep inner text
        html = re.sub(r'<span class="icon[^"]*">(.*?)</span>', r'\1', html)
        return html.strip()

    def extract(self, entry):
        title = entry.get('title')
        date = self._format_date(entry.get('published', ''))
        description = entry.get('summary', '')

        # Extract first image from description
        image_match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', description)
        image_src = image_match.group(1) if image_match else None

        description = self._clean_html(description)

        return image_src, title, date, description

    def convert(self, image_src, title, date, content):
        md_image = MarkdownConverter.image_tag(image_src, "news_image", 100)
        md_title = MarkdownConverter.h2(title)
        md_date = MarkdownConverter.p(date)
        md_content = MarkdownConverter.br(content)
        return "".join([md_image, md_title, md_date, md_content])

    def fetch_and_convert(self):
        try:
            entry = self.fetch_latest()
            if entry is None:
                return "No news available."
            image_src, title, date, content = self.extract(entry)
        except Exception as e:
            return str(e)
        return self.convert(image_src, title, date, content)


if __name__ == "__main__":
    ios_dev_news = iOSDevNewsRSS()
    with open('./README.md', 'w') as readme:
        with open('./info.md', 'r') as info:
            for line in info.readlines():
                readme.write(line)
        news = ios_dev_news.fetch_and_convert()
        readme.write(news)
