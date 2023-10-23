import scrapy
from realestate import items
from scrapy.loader import ItemLoader


class Domiporta1Spider(scrapy.Spider):
    name = "domiporta1"
    allowed_domains = ["domiporta.pl"]
    start_urls = ["https://www.domiporta.pl/mieszkanie/sprzedam"]

    def parse(self, response):

        for links in response.xpath("//*[@class='grid-item grid-item--cover']"):
            link = links.xpath(".//a[@class='sneakpeak__title']/@href").get()
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

        loader = ItemLoader(item = items.RealestateItem(), response=response)
        
        if response.xpath("//span[@class='features__item_value features__item_value--price']/p/text()").get() is not None:
            loader.add_value('price', response.xpath("//span[@class='features__item_value features__item_value--price']/p/text()").get())
        else:
            loader.add_value('price', 'n/a')
        
        if response.xpath("//span[text()='Numer oferty']/following-sibling::span/text()").get() is not None:
            loader.add_value('offer_number', response.xpath("//span[text()='Numer oferty']/following-sibling::span/text()").get())
        else:
            loader.add_value('offer_number', 'n/a')

        if response.xpath("//span[contains(text(),'Materiał')]/following-sibling::span/text()").get() is not None:
            loader.add_value('material', response.xpath("//span[contains(text(),'Materiał')]/following-sibling::span/text()").get())
        else:
            loader.add_value('material', 'n/a')

        if response.xpath("//span[contains(text(),'Powierzchnia całkowita')]/following-sibling::span/text()").get() is not None:
            loader.add_value('square_footage', response.xpath("//span[contains(text(),'Powierzchnia całkowita')]/following-sibling::span/text()").get())
        else:
            loader.add_value('square_footage', 'n/a')

        if response.xpath("//span[contains(text(),'Rok budowy')]/following-sibling::span/text()").get() is not None:
            loader.add_value('construction_year',response.xpath("//span[contains(text(),'Rok budowy')]/following-sibling::span/text()").get())
        else:
            loader.add_value('construction_year', 'n/a')

        if response.xpath("//span[contains(text(),'Liczba pokoi')]/following-sibling::span/text()").get() is not None:
            loader.add_value('number_of_rooms',response.xpath("//span[contains(text(),'Liczba pokoi')]/following-sibling::span/text()").get())
        else:
            loader.add_value('number_of_rooms', 'n/a')

        if response.xpath("//span[contains(text(),'Cena za')]/following-sibling::span/text()").get() is not None:
            loader.add_value('price_per_m2',response.xpath("//span[contains(text(),'Cena za')]/following-sibling::span/text()").get())
        else:
            loader.add_value('price_per_m2', 'n/a')

        if response.xpath("//span[@itemprop='addressLocality']/text()").get() is not None:
            loader.add_value('city',response.xpath("//span[@itemprop='addressLocality']/text()").get())
        else:
            loader.add_value('city', 'n/a')

        if response.xpath("//span[@itemprop='streetAddress']/text()").get() is not None:
            loader.add_value('address',response.xpath("//span[@itemprop='streetAddress']/text()").get())
        else:
            loader.add_value('address', 'n/a')

        if response.xpath("//meta[@itemprop='addressRegion']/@content").get() is not None:
            loader.add_value('region',response.xpath("//meta[@itemprop='addressRegion']/@content").get())
        else:
            loader.add_value('region', 'n/a')

        yield loader.load_item()

  

 #jupyter/base-notebook