# encoding:utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from liah8_TGB.items import Liah8TgbItem
u'''
scrapy crawl TGB -o 原來TGB.json -t json
gzip 原來TGB.json
'''
class Bang7Loo7Spider(CrawlSpider):
	name = "liah8"
	allowed_domains = ["taioanchouhap.pixnet.net",
					   'taioan-chouhap.myweb.hinet.net']
	start_urls = [
		"http://taioanchouhap.pixnet.net/blog",
		"http://taioan-chouhap.myweb.hinet.net/0_boklok.htm",
		'http://taioanchouhap.pixnet.net/blog/post/177926499',
	]
	
	rules = [
		Rule(
			SgmlLinkExtractor(allow=[".*", ]),
			callback="parse_context", follow=False
		),
    ]
	def parse_context(self, response):
		sel = Selector(response)
		item = Liah8TgbItem()
		item['url'] = response.url
		item['title'] = sel.css('li.publish').extract()
		item['date'] = sel.css('li.title').extract()
		item['context'] = sel.css('div.article-content-inner').extract()
		yield item