from scrapy import Item,Field

class RealestateItem(Item):
    price = Field()
    offer_number = Field()
    
