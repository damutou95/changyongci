# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChangyongciItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    changyongci = scrapy.Field()
    shiyongpinlv = scrapy.Field()
