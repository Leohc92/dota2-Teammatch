# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem


class DotabuffPipeline(object):

	def open_spider(self, spider):
		self.match_dict = {}

	def process_item(self, item, spider):
		ID = item['matchID']
		if ID in self.match_dict:
			self.match_dict[ID] =  self.match_dict[ID] + 1
			if self.match_dict[ID]==5:
				return item
			else:
				raise DropItem("Drop item: %s" % item)
		else:
			self.match_dict[ID] = 1
			raise DropItem("Drop item: %s" % item)