# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import json
import re
import asyncio
class OneNewsSpider(scrapy.Spider):
    name = 'bruhspider'
    custom_settings = {
        'DOWNLOAD_DELAY' : '2',
        'CONCURRENT_REQUESTS' : '6'
    }
    allowed_domains = ['ioi.dk']
    start_urls = []
    all_urls = []
    with open('news.json') as json_file:
        data = json.load(json_file)
    for i in range(len(data)):
        all_urls.append(data[i]['news_url'])
    start_urls.append(all_urls[0])
    m = 0
    def parse(self, response):
        yield{
            'title': response.xpath('//*[@id="ajax-content-wrap"]/div[2]/div/div[1]/div/h1/text()').get(),
            'date': response.xpath('//*[@id="single-below-header"]/span[1]/text()').get(),
            'text': re.sub(r'\<[^>]*\>', '', response.xpath('//*[@id="post-area"]').get()),
            'url' : self.all_urls[self.m]
        }
        self.m = self.m + 1
        next_page = self.all_urls[self.m]
        if next_page is not (None):
            yield response.follow(next_page, callback=self.parse)
#re.sub(r'\<[^>]*\>', '', 
#\\[a-z][0-9]*
class NewsSpider(scrapy.Spider):
    name = 'newspider'
    allowed_domains = ['ioi.dk']
    start_urls = ['https://ioi.dk/news']
    def parse(self, response):
        n = 1
        m = 1
        xpath1 = "//*[@id='post-area']/div/div/div["+ str(n) + "]/div["+ str(m)+ "]/a"

        while n < 5:
            while m <= 2:
                yield{
                    'news_url': response.xpath(xpath1+"/@href").get(),
                    'title': response.xpath(xpath1+"/div/div[2]/h3/text()").get(),
                    'date': response.xpath(xpath1+"/div/div[2]/span/text()").get(),
                    'text': response.xpath(xpath1+"/div/div[3]/p/text()").get()
                }
                m = m + 1
                xpath1 = "//*[@id='post-area']/div/div/div["+ str(n) + "]/div["+ str(m)+ "]/a"
            n = n + 1
            m = 1
            xpath1 = "//*[@id='post-area']/div/div/div["+ str(n) + "]/div["+ str(m)+ "]/a"
        next_page = response.css('#pagination > div.next > a::attr(href)').get()
        if next_page is not (None):
            yield response.follow(next_page, callback=self.parse)
#//*[@id="post-area"]/div/div/div[1]/div[1]/a/div/div[2]/h3
#//*[@id="post-area"]/div/div/div[1]/div[1]/a/div/div[2]/span