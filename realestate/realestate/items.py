from scrapy import Item,Field
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst, Compose

def remove_currency(value):
    if value is not '0':
        return value.strip().replace('\xa0','').replace(' zł','')
    else:
        return value

def name_parse(value):
    if value:
        return value.replace("'", '')

def remove_square_meters(value):
    if value:
        return value.replace('/m','')

def square_footage_strip(value):
    if value:
        return value.replace(' m','')

class RealestateItem(Item):
    price = Field(
        input_processor = MapCompose(remove_currency),
        output_processor = TakeFirst()
    )
    offer_number = Field(
        output_processor = TakeFirst()
    )
    material = Field(
        output_processor = TakeFirst()
    )
    square_footage = Field(
        input_processor = MapCompose(square_footage_strip),
        output_processor = TakeFirst()
    )
    construction_year = Field(
        output_processor = TakeFirst()
    )
    number_of_rooms = Field(
        output_processor = TakeFirst()
    )
    price_per_m2 = Field(
        input_processor= MapCompose(remove_currency, remove_square_meters),
        output_processor = TakeFirst()
    )
    city = Field(
        input_processor = MapCompose(name_parse),
        output_processor = TakeFirst()
        )
    address = Field(
        input_processor = MapCompose(name_parse),
        output_processor = TakeFirst()
    )
    region = Field(
        output_processor = TakeFirst()
    )