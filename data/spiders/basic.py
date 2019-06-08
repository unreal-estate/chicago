# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['cityofchicago.org']
    start_urls = ['http://cityofchicago.org/']

    def parse(self, response):
        pass
