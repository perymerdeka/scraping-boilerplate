import logging

from bs4 import BeautifulSoup

from spider.sites.detik.parser import SiteParser
from spider.sites.detik.response import SiteResponse
from spider.config import SpiderConfig as cfg


class DetikSpider(object):
    def __init__(self):
        self.base_url = "https://news.detik.com"
        self.parser = SiteParser(base_url=self.base_url)
        self.response = SiteResponse(base_url=self.base_url)

    def generate_pages(self):
        if cfg.DEBUG:
            logging.debug("Generate Contents Run In Debug Mode")
            f = open(f"{cfg.TEMP_DIR}/detik.html", "r")
            soup = BeautifulSoup(f.read(), "html.parser")
        else:
            soup = self.response.response(url=f"{self.base_url}/jabodetabek/")
        
        titles = self.parser.parse_title(soup=soup)

        return titles

