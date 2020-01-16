from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import IphoneBlackFridayBuyAppleIphonesOnlineItem, PortiaItem


class JumiaCoKe(BasePortiaSpider):
    name = "jumia"
    allowed_domains = ['www.jumia.co.ke']
    start_urls = ['https://www.jumia.co.ke/']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                IphoneBlackFridayBuyAppleIphonesOnlineItem,
                None,
                '.sku',
                [
                    Field(
                        'ur',
                        '.link::attr(href)',
                        []),
                    Field(
                        'name',
                        '.link > .title > .name *::text',
                        []),
                    Field(
                        'discount',
                        '.link > .price-container > .sale-flag-percent *::text',
                        []),
                    Field(
                        'price',
                        '.link > .price-container > .price-box > span:nth-child(1) > span:nth-child(2) *::text',
                        [])])]]
