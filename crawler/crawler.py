import requests 
from bs4 import BeautifulSoup 
from lxml import etree
import time
from time import sleep 
import csv

for x in range(1,3):

    #代理，可以去github搜索ipproxy，有免费ip代理项目

    url = 'https://www.janes.com/sea-news-list/{}'.format(x) 
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers, timeout = 10) 

    response.encoding = response.apparent_encoding
    page_content = response.text
    parse = etree.HTML(page_content)
    url_list = parse.xpath('//div[@class = "list-item border-bottom border-primary px-3 pb-2 py-3"]/a')

    for url in url_list:
        url = {'head' : url.xpath('./h3/text()')[0],
            'a_href' : url.xpath('./@href')[0]
        }
        #print(url)

        with open("JanesNews.csv", 'a', encoding = 'utf_8_sig', newline = '') as fp:
            fieldnames = ['head', 'a_href']
            writer = csv.DictWriter(fp, fieldnames)
            writer.writerow(url)