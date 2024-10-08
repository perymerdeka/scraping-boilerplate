from spider.sites.detik.spider import DetikSpider

def main():
    detik = DetikSpider()
    print(detik.generate_pages())

if __name__ == '__main__':
    main()