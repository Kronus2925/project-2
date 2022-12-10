import scrapy

class Domiporta1Spider(scrapy.Spider):
    name = "domiporta1"
    allowed_domains = ["domiporta.pl"]
    start_urls = ["https://www.domiporta.pl/mieszkanie/sprzedam"]

    def parse(self, response):

        for links in response.xpath("//*[@class='grid-item grid-item--cover']"):
            link = links.xpath("//a[@class='sneakpeak__title']/@href").get()
            offer_link = f"https://www.domiporta.pl{link}"
            yield scrapy.Request(offer_link, callback=self.parse_items)

        next_page = response.xpath(
            "//li[@class='pagination__link pagination__link--right']//a/@href"
        ).get()
        print(next_page)
        if next_page:
            next_page_url = f"https://www.domiporta.pl{next_page}"
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_items(self, response):

        yield {
            "price": response.xpath(
                "//span[@class='features__item_value features__item_value--price']/p/text()"
            ).get(),
            "offer_number": response.xpath(
                "//span[normalize-space()='Numer oferty']/span/text()"
            ).get(),
        }
