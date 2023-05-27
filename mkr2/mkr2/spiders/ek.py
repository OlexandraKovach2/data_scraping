import scrapy
from mkr2.SeleniumRequest import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions 
from mkr2.items import PrinterItem

class EkSpider(scrapy.Spider):
    name = "ek"
    allowed_domains = ["ek.ua"]
    start_urls = [f"https://ek.ua/ua/list/163/{page}/" for page in range(0,3)]
    def start_requests(self):   
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=2
            )
            
    def parse(self, response):
        for card in response.css('div.model-short-div.list-item--goods'):
            name = card.css("span.u::text").get()
            image_url = card.css("img::attr(src)").get()
            shop_list = card.css('table.model-hot-prices u::text').getall()
            price_list = card.css('table.model-hot-prices a::text').getall()
            for item in price_list:
                if(item == ' ' or item == '\xa0'):
                    price_list.remove(item)
            else:
                for i in range(len(price_list)):
                    price_list[i] = price_list[i].replace(u'\xa0', u'')
                    price_list[i] = price_list[i].replace('грн.', '')
                price_list = list(filter(lambda a: a != '', price_list))
            if(len(shop_list) != 0 and shop_list != [None]):
                for i in range(len(shop_list)):
                    yield PrinterItem (
                        name = name,
                        image_urls = [image_url],
                        shop = shop_list[i],
                        price = price_list[i]
                    )