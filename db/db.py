SELECT_ALL_PRODUCTS = "SELECT * FROM product"
INSERT_PRODUCT = "INSERT INTO product(name, price, age, weight, rating) VALUES (?, ?, ?, ?, ?)"
SELECT_PRODUCT = "SELECT id, name, price, age, weight, rating FROM product WHERE id = ?"
DELETE_PRODUCT = "DELETE FROM product WHERE id = ?"

SELECT_ALL_CLIENTS = "SELECT * FROM client"
INSERT_CLIENT = "INSERT INTO client(name, age) VALUES (?, ?)"
SELECT_CLIENT = "SELECT id, name, age, product_id FROM client WHERE id = ?"
GET_CLIENT_WITH_PRODUCT = """SELECT c.name, c.age, s.name, s.price, s.age, s.weight, s.rating 
FROM client AS c LEFT JOIN product AS s ON c.product_id = s.id WHERE c.id = ?"""
DELETE_CLIENT = "DELETE FROM client WHERE id = ?"
ADD_PRODUCT_ID_FOR_CLIENT = "UPDATE client SET product_id = ? WHERE id = ?"

class Database:
    def __init__(self, db):
        self.db = db
        self.cursor = db.cursor()

    def insert_product(self, name, price, age, weight, rating):
        self.cursor.execute(INSERT_PRODUCT, [name, price, age, weight, rating])
        self.db.commit()
        return True

    def get_product_by_id(self, id):
        self.cursor.execute(SELECT_PRODUCT, [id])
        return self.cursor.fetchone()

    def del_product_by_id(self, id):
        self.cursor.execute(DELETE_PRODUCT, [id])
        self.db.commit()
        return self.cursor.fetchall()

    def get_products(self):
        self.cursor.execute()
        return self.cursor.fetchall()

    def get_clients(self):
        self.cursor.execute(SELECT_ALL_CLIENTS)
        return self.cursor.fetchall()

    def insert_client(self, name, age):
        self.cursor.execute(INSERT_CLIENT, [name, age])
        self.db.commit()
        return True

    def get_client_by_id(self, id):
        self.cursor.execute(SELECT_CLIENT, [id])
        return self.cursor.fetchone()

    def get_client_with_product(self, id):
        self.cursor.execute(GET_CLIENT_WITH_PRODUCT, [id])
        return self.cursor.fetchone()

    def del_client_by_id(self, id):
        self.cursor.execute(DELETE_CLIENT, [id])
        self.db.commit()
        return self.cursor.fetchall()

    def add_product_id_for_client(self, product_id, id):
        self.cursor.execute(ADD_PRODUCT_ID_FOR_CLIENT, [product_id, id])
        self.db.commit()
        return True

    def create_tables(self):
        tables = [
            """CREATE TABLE IF NOT EXISTS product(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    age INTEGER NOT NULL,
                    weight INTEGER NOT NULL,
                    rating INTEGER NOT NULL
                )
            """,
            """CREATE TABLE IF NOT EXISTS client(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    product_id INTEGER
                )
            """

        ]
        cursor = self.db.cursor()
        for table in tables:
            cursor.execute(table)