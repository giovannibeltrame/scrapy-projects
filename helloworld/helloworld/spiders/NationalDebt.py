import scrapy


class NationaldebtSpider(scrapy.Spider):
    name = "NationalDebt"
    allowed_domains = ["worldpopulationreview.com"]
    start_urls = ["https://worldpopulationreview.com/country-rankings/countries-by-national-debt"]

    def parse(self, response):
        tableLines = response.xpath("(//tbody)[1]/tr")
        for line in tableLines:
            country = line.xpath(".//td[1]/span/a/text()").get()
            gdp = line.xpath(".//td[2]/span/text()").get()

            yield {
                'country': country,
                'gdp': gdp
            }
