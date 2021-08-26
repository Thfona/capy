import re

regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


class Validator():
    def __init__(self):
        super().__init__()

    def validate_url(self, url):
      return re.match(regex, url) is not None

    def validate_youtube_url(self, url):
      return self.validate_url(self, url) and 'youtube.com' in url
