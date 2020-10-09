# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
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