# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
import json
from dotabuff.items import DotabuffItem

class DotaSpider(CrawlSpider):
	name = "dotaspider"
	allow_domains = ['www.dotabuff.com']
	start_urls = []
	with open('spiders/Steam.json','r') as f:
		steam_data = json.load(f)
		f.close
	steam_members = steam_data['members']
	for member in steam_members:
		url = 'http://www.dotabuff.com/players/%s/matches?page=1' %str(member['steamID']-76561197960265728)
		start_urls.append(url)

	rules = (Rule(LinkExtractor(allow=(r'http://www.dotabuff.com/players/\d+/matches\?page=\d+')), callback="parse_item", follow= True),)

	def parse_item(self, response):
		sel = Selector(response)
		items = []
		matches = sel.xpath('//td[@class="cell-large"]/a/@href').extract()
		for match in matches:
			item = DotabuffItem()
			item['matchID'] = match
			items.append(item)
		return  items
		