# -*- coding: utf-8 -*-
import scrapy
import json

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [api_url.format(1)]


    def parse(self, response):
        data = json.loads(response.text)
        for quote in data['quotes']:
            # generate the items we want:
            yield {
                'author_name': quote['author']['name'],
                'text': quote['text'],
                'tags': quote['tags'],
            }
#             to make sure it goes on to all the pages

        if data ['has_next']:
            nex_page = data['page'] + 1
            # generate a new request for the next page
            yield scrapy.Request(url=self.api_url.format(nex_page), callback=self.parse)
