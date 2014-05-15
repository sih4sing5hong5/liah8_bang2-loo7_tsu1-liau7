# encoding:utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spider import Spider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from liah8_bang7_loo7_tsu1_liau7.items import HtmlItem
from scrapy.http.request import Request
from urlparse import urljoin
u'''
scrapy crawl liah8 -o data.json -t json
gzip data.json
'''
class Bang7Loo7Spider(Spider):
	name = "liah8"
	allowed_domains = [
		"xn--v0qr21b.xn--kpry57d",
		]
	start_urls = [
		"http://xn--v0qr21b.xn--kpry57d",
		"http://xn--v0qr21b.xn--kpry57d/assets/pan2_hing5/ituanLOGO_1.png",
# 		'http://xn--v0qr21b.xn--kpry57d/%E8%A8%80%E8%AA%9E%E8%B3%87%E6%96%99%E5%BA%AB/%E8%87%BA%E7%81%A3%E8%A8%80%E8%AA%9E%E5%B7%A5%E5%85%B71021127.sql.bz2',
	]
	not_html_suffix=['css','js','png','jpg','gif','tiff','gz','bz2','7z','rar',
		'CSS','JS','PNG','JPG','GIF','TIFF','GZ','BZ2','7Z','RAR']

	def parse(self, response):
		isHtml=False
		if 'text/html' in response.headers['Content-Type']:
			isHtml=True
			
		print("response.headers['Content-Type']",response.headers['Content-Type'],isHtml)
		if isHtml:
			item = HtmlItem()
			item['url'] = response.url
# 			item['html'] = response.body
			sel = Selector(response)
			for a in sel.css('a::attr(href)'):
				href=a.extract()
				if href.split('.')[-1] not in self.not_html_suffix: 
					yield Request(
						url=urljoin(response.url, href),
						callback=self.parse)
# 				yield Request(url=a.extract(),callback=self.parse)
			yield item