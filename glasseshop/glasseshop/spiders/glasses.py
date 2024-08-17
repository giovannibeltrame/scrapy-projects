import scrapy


class GlassesSpider(scrapy.Spider):
    name = "glasses"
    allowed_domains = ["www.glassesshop.com"]
    start_urls = ["https://www.glassesshop.com/bestsellers"]

    def parse(self, response):
        for product in response.xpath("//div[@id='product-lists']/div[contains(@class, 'product-list-item')]"):

            name = product.xpath(".//div[@class='p-title']/a[not(contains(@class, 'none'))]/@title").get()
            color = product.xpath(".//span[@class='product-color active']/@title").get()
            url = product.xpath(".//div[@class='product-img-outer']/a/@href").get()
            image_url = product.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@data-src").get()
            price = product.xpath(".//div[@class='p-price']//span/text()").get()

            yield {
                'url': url,
                'image_url': image_url,
                'name': f"{name} - {color}",
                'price': price
            }

        next_page = response.xpath("//ul[@class='pagination']/li[last()]/a[@rel='next']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)


