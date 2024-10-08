import requests

from bs4 import BeautifulSoup
from typing import Any

from spider.config import SpiderConfig as cfg


class SiteResponse(object):

    def __init__(self, base_url: str):
        self.base_url: str = base_url

    def response(self, url: str = ""):
        headers: dict[str, Any] = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9,id;q=0.8,ar;q=0.7,ru;q=0.6",
            "cache-control": "max-age=0",
            "cookie": "visid_incap_3108313=eAZjfFTnQK6Z4sZp8/MkJupP9WYAAAAAQUIPAAAAAABMq3NEx6PYhinQzhid6CCd; incap_ses_1848_3108313=npXGD6OLayEIVjbYRWqlGepP9WYAAAAAw7pCvfVhvvyin4cZIFE42w==; FCNEC=%5B%5B%22AKsRol_2TI7S1eP0gfDn-DxO7ND01FH47xPAhw4MNutUnQ-yHiBh1Eqgp7CIKP8_9zf-hpWTGmtjO3mWzU1UNCMExfHUCwQIkghq4U9eIFYmVka-1XjxC0l_APEL4pxzzOZ_z04qktGw3KKPDxWi3jXKHo-ZNScOQg%3D%3D%22%5D%5D; __gads=ID=98b5d9831842b70a:T=1727352817:RT=1727352817:S=ALNI_Mb8DiH5j-_Bwx1ectc2FlZFEzwCcg; __gpi=UID=00000f1eb6f09993:T=1727352817:RT=1727352817:S=ALNI_MarGkETfIM91jLChy8kbYvp8EKAAA; __eoi=ID=5a51ae0b792fcaaa:T=1727352817:RT=1727352817:S=AA-AfjbNxMmeXf5ruokL_pF0wDYG",
            "priority": "u=0, i",
            "sec-ch-ua": '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }
        res = requests.get(url=url, headers=headers)
        print(f"Process URL: {res.url}")
        if res.status_code == 200:
            print(f"Request success with status code {res.status_code}")
            if cfg.DEBUG:
                f = open(f"{cfg.TEMP_DIR}/detik.html", "w+")
                f.write(res.text)
                f.close()

            soup: BeautifulSoup = BeautifulSoup(res.content, "html.parser")
            return soup
        else:
            raise Exception(f"Request failed with status code {res.status_code}")
