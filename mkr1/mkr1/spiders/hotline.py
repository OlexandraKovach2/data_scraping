import scrapy


class HotlineSpider(scrapy.Spider):
    name = "hotline"
    allowed_domains = ["hotline.ua"]
    start_urls = ["https://hotline.ua/ua/musical_instruments/elektrogitary/"]

    def parse(self, response):
        names = response.xpath('//a[contains(@class, "list-item__title")]/text()').getall()
        prices = response.xpath('//span[contains(@class, "price__value")]/text()').getall()
        for i in range(len(names)):
            print(names[i])
            print(prices[i])
