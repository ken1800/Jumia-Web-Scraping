# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from main.models import Perfecto
class PerfectoPipeline(object):
    def process_item(self, item, spider):
        jumia = Perfecto()
        
        jumia.discount = item['discount']
        jumia.name = item['name']
        jumia.price = item['price']
        jumia.link = item['ur']
        
        jumia.save()
        return item