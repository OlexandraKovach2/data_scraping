import scrapy
from mkr2.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from mkr2.items import EkatalogItem

class EkatalogSpider(scrapy.Spider):
    name = "ekatalog"
    allowed_domains = ["ek.ua"]
    start_urls = [f"https://ek.ua/ua/list/161/{page}/" for page in range(1,20)]
    #я тут зробила лише 20 сторінок бо їх там аж 404 і процес зборки даних займає дуже великий час
    def start_requests(self):   
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=0
            )
        
    def parse(self, response):
        for card in response.xpath('//div[contains(@class, "model-short-div") and contains(@class, "list-item--goods")]'):
            shop_list = card.xpath('.//table[contains(@class, "model-hot-prices")]//u/text()').getall()
            price_list = card.xpath('.//table[contains(@class, "model-hot-prices")]//a/text()').getall()

            if len(shop_list) == 0:
                shop_list = [card.xpath('.//div[contains(@class, "pr31-sh") and contains(@class, "posr")]//u/text()').get()]
                price_list = [card.xpath('.//div[contains(@class, "pr31") and contains(@class, "ib")]//span/text()').get()]

            price_list = [item for item in price_list if item.strip() != '' and item.strip() != '\xa0']
            price_list = [item.replace(u'\xa0', u'').replace('грн.', '') for item in price_list]

            yield EkatalogItem(
                name=card.xpath('.//span[contains(@class, "u")]/text()').get(),
                img_src=card.xpath('.//img/@src').get(),
                shop_list=shop_list,
                price_list=price_list
            )
