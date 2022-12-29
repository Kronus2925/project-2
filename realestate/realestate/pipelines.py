import psycopg2


class RealestatePipeline:
    def __init__(self):

        self.conn = psycopg2.connect(
            dbname="postgres",
            user="Kuba",
            password="postgres",
            host="localhost",
            port="5432",
        )

        self.cur = self.conn.cursor()

        self.cur.execute(
            """CREATE TABLE IF NOT EXISTS offers(price varchar(100), offer_number varchar(100), material varchar(100), square_footage varchar(100), construction_year varchar(100), number_of_rooms varchar(100), price_per_m2 varchar(100), city varchar(100), address varchar(100), region varchar(100))"""
        )

    def process_item(self, item, spider):

        self.cur.execute(
            f"INSERT INTO offers (price, offer_number, material, square_footage, construction_year, number_of_rooms, price_per_m2, city, address, region) VALUES ('{item['price']}', '{item['offer_number']}', '{item['material']}', '{item['square_footage']}', '{item['construction_year']}', '{item['number_of_rooms']}', '{item['price_per_m2']}', '{item['city']}', '{item['address']}', '{item['region']}')"
        )
        self.conn.commit()
        return item

    def close_spider(self, spider):

        self.cur.close()
        self.conn.close()
