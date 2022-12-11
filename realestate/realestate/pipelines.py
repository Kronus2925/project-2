import psycopg2

class RealestatePipeline:

    def __init__(self):

        self.conn = psycopg2.connect(
            dbname= "postgres",
            user= "Kuba", 
            password= "postgres",
            host="/tmp/",
            )

        self.cur = self.conn.cursor()

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS offers(
            id int NOTNULL auto_increment,
            price varchar(100),
            material varchar(100),
            offer_name varchar(100),
            construction_year varchar(100),
            square_footage varchar(100),
            number_of_rooms varchar(100),
            price_per_m2 varchar(100),
            city varchar(100),
            address varchar(100),
            region varchar(100),

        )
        ''')
    def process_item(self, item, spider):

        self.cur.execute(f'''
        INSERT INTO offers (price, offer_name) VALUES ({item['price'], item['offer_name']})
        ''')
        self.conn.commit

    def close_spider(self, spider):
        
        self.cur.close()
        self.conn.close()
