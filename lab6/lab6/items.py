# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Lab6Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class CountryItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    links_inside = scrapy.Field()
class HotlineItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    image_urls = scrapy.Field()
