import scrapy
from lab2.items import UzhnuHref

class UzhnuSpider(scrapy.Spider):
    name = "uzhnu"
    allowed_domains = ["www.uzhnu.edu.ua"]
    start_urls = ["http://www.uzhnu.edu.ua/"]
    links = []
    def parse(self, response):
        for link in response.xpath("//a/@href").getall():
            if link is not None:
                if link not in self.links:
                    if 'https' in link: 
                        self.links.append(link)
                        yield UzhnuHref (
                            href = link
                        )
        locallinks = self.links
        for link in locallinks:
            yield scrapy.Request(link, self.parse_child_page)
    def parse_child_page(self, response):
        try: 
            allhref = response.css("a::attr(href)").getall()
            for link in allhref:
                if link is not None:
                    if link not in self.links:
                        if 'https' in link: 
                            self.links.append(link)
                            yield UzhnuHref (
                                href = link
                            )
        except:
            print(f"can't parse href from this URL: {response.request.url}")