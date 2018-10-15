# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SrapItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    papername = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    released = scrapy.Field()
    url = scrapy.Field()
    imgl = scrapy.Field()
