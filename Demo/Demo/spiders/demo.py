# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import quote
from Demo.items import  DemoItem

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['s.weibo.com']
    start_urls = ['http://s.weibo.com/']

    def start_requests(self):
        base_url='http://s.weibo.com/'
        key="广州塔"
        params=['article?q=']
        for i in params:
            url=base_url+i+quote(key)
            yield  Request(url,callback=self.parse)


    def parse(self, response):
            article=response.xpath('//div[@class=card-article-a]')
            for data in article:
                item = DemoItem()
                item['title']=data.xpath('//h3/a/@title').extract()
                item['title_url']=data.xpath('//h3/a/@href').extract()
                #item['author']=article.xpath('//div[@class="act"]/span[1]/a/text()')
                #item['time']=article.xpath('//div[@class="act"]/span[2]/text()')
                yield item

