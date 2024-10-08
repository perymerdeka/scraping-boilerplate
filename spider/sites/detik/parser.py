from bs4 import BeautifulSoup
from typing import Any
from pathlib import Path
from os.path import basename

from spider.sites.detik.response import SiteResponse

class SiteParser(object):
    """Class to Parse Sites
    """
    def __init__(self, base_url: str):
        self.base_url: str 
        self.response: SiteResponse = SiteResponse(base_url=base_url)
        self.formatted_data: dict[str,Any] = {
            "title": f"{basename(Path(__file__).parent)}",
            "contents": []
        }
   
    def parse_title(self, soup: BeautifulSoup) -> list[dict[str, Any]]:
        content = soup.find_all('article', attrs={'class': 'ph_newsfeed_d article_inview list-content__item'})
        for index, c in enumerate(content):
            print(f"Process Content {index} of {len(content)}")
            title = c.find('h3', attrs={'class': 'media__title'}).text.strip()
            link = c.find('h3', attrs={'class': 'media__title'}).find('a')['href']
            date = c.find('div', attrs={'class': 'media__date'}).find('span')['title']

            data_dict: dict[str, Any] = {
                "title": title,
                "date": date,
                "link": link,
                "detail": self.parse_detail_contents(url=link)

            }
            self.formatted_data['contents'].append(data_dict)
        return self.formatted_data['contents']
    
    def parse_detail_contents(self, url) -> list[dict[str, Any]]:
        soup = self.response.response(url=url)
        author = soup.find('div', attrs={'class': 'detail__author'}).text.strip()
        contents = soup.find('article', attrs={'class': 'detail'}).text.strip()
        data_dict: dict[str, Any] = {
            "author": author,
            "contents": contents

        }
        return data_dict

