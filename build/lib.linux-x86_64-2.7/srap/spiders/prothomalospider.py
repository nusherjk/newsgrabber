# -*- coding: utf-8 -*-
#BUGS
#1.prothomalo.com/economy/article is not being grabbed(Fixed)
#2.image link is not being grabbed (fixed)

#Reminder
#need to add the basic url(DONE)

#stop spider from crawling(Done)
    #take the item['released'] and make date contrains to stop crawler
    #raise CloseSpider


import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from srap.items import SrapItem
from scrapy.exceptions import CloseSpider

class ProthomalospiderSpider(CrawlSpider):
    name = 'pa'

    allowed_domains = ['prothomalo.com']
    start_urls = ['http://prothomalo.com/economy/article']
#rules for crawlspider to go through
    rules = (
        Rule(LinkExtractor(allow=('/?page=\d',),unique=True,),callback='parse_start_url',follow=True,),
             )
#parse data from the lists of news
    def parse_start_url(self, response):
        BASIC_URL = 'http://prothomalo.com'
        data = response.css('div#widget_54678 > div > div.contents.summery_view.shaded_bg > div > div ')
        item = SrapItem()
        for d in data:
            item['papername'] = 'Prothom Alo'
            item['title'] =d.css('div > div.info.has_ai > h2 > span::text').extract()[0]
            item['content'] = d.css('div > div.info.has_ai > div.summery::text').extract()[0]
            item['released'] = d.css('div > div.info.has_ai > div.additional > span.time.aitm::attr(data-published)').extract()[0]
            item['url'] = BASIC_URL + d.css('div > a::attr(href)').extract()[0]
            item['imgl'] = d.css('div > div.image img::attr(src)').extract()[0]
            #if item['released'][:7]!='2018-05':
            #    raise CloseSpider(reason="Process Finished")

            yield item






#data-published="2018-05-01T00:00:00+06:00"

