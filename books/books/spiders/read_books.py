import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ReadBooksSpider(CrawlSpider):
    name = "read_books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article/h3/a"), callback="parse_item", follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a")),
        )

    def parse_item(self, response):
        rating = response.xpath("//div[contains(@class, 'product_main')]/p[contains(@class, 'star-rating')]/@class").get()
        yield {
            "name": response.xpath("//h1/text()").get(),
            "price": response.xpath("//h1/following-sibling::p[1]/text()").get(),
            "cover_image_url": response.urljoin(response.xpath("//div[@class='item active']/img/@src").get()),
            "rating": rating.replace("star-rating ", ""),
        }
