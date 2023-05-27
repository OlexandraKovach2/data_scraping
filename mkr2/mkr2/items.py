# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class PrinterItem(scrapy.Item):
    name = scrapy.Field()
    image_urls = scrapy.Field()
    price = scrapy.Field()
    shop = scrapy.Field()
    
class Mkr2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
