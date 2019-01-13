# -*- coding: utf-8 -*-
import scrapy
from changyongci import settings
from scrapy import Request
from changyongci.items import ChangyongciItem
class WordSpider(scrapy.Spider):
    name = 'word'
    #allowed_domains = ['sss']
    start_urls = ['https://github.com/hermitdave/FrequencyWords/blob/master/content/2016/en/en_50k.txt']
    headers = settings.HEADERS
    def start_requests(self):
        yield Request(self.start_urls[0],callback=self.parse,headers=self.headers)

    def parse(self, response):
        #获取常用词集合
        set = response.xpath('//table/tr')
        for s in set:
            item = ChangyongciItem()

            item['changyongci'] = s.xpath('./td[@class="blob-code blob-code-inner js-file-line"]/text()').extract_first().split()[0]
            item['shiyongpinlv'] = s.xpath('./td[@class="blob-code blob-code-inner js-file-line"]/text()').extract_first().split()[1]
            yield item
