import sqlite3

CREATE_PRODUCTS_TABLE = "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name Text, price float);"
CREATE_COURIERS_TABLE = "CREATE TABLE IF NOT EXISTS couriers (id INTEGER PRIMARY KEY, name Text, phone integer);"
CREATE_ORDER_STATUS_TABLE = "CREATE TABLE IF NOT EXISTS order_status(id INTEGER PRIMARY KEY, order_status Text);"
CREATE_ORDERS_TABLE = """
CREATE TABLE IF NOT EXISTS orders (
id INTEGER PRIMARY KEY,
customer_name text,
customer_address text,
customer_phone text,
courier integer,
status integer,
items text);"""

INSERT_PRODUCT = "INSERT INTO products (name, price) VALUES (?,?);"
INSERT_COURIER = "INSERT INTO couriers (name, phone) VALUES (?,?);"
INSERT_ORDER_STATUS = "INSERT INTO order_status (order_status) VALUES (?);"
INSERT_ORDER = "INSERT INTO orders (customer_name,customer_address,customer_phone,courier,status,items) VALUES (?,?,?,?,?,?);"

UPDATE_PRODUCT = """
UPDATE products
SET name = ?, price = ?
WHERE id = ?;"""

UPDATE_COURIER = """
UPDATE couriers
SET name = ?, phone = ?
WHERE id = ?;"""

UPDATE_ORDER = """
UPDATE orders
SET customer_name = ?,
customer_address = ?,
customer_phone = ?,
courier = ?,
items = ?
WHERE id = ?;"""

UPDATE_ORDER_STATUS = """
UPDATE orders
SET status = ?
WHERE id = ?;"""

GET_ALL_PRODUCTS = "SELECT * FROM products;"
GET_ALL_COURIERS = "SELECT * FROM couriers;"
GET_ALL_ORDERS = "SELECT * FROM orders;"
GET_ALL_ORDER_STATUS = "SELECT * FROM order_status"

GET_PRODUCTS_BY_NAME = "SELECT * FROM products WHERE name = ?;"

GET_PRODUCTS_BY_ID = "SELECT * FROM products WHERE id = ?;"
GET_COURIERS_BY_ID = "SELECT * FROM couriers WHERE id = ?;"
GET_ORDERS_BY_ID = "SELECT * FROM orders WHERE id = ?;"

GET_PRODUCTS_BY_PRICE = """
SELECT * FROM products
ORDER BY price DESC
LIMIT 10;"""

DELETE_PRODUCT = "DELETE FROM products WHERE name = ?;"
DELETE_PRODUCT_BY_ID = "DELETE FROM products WHERE id = ?;"
DELETE_COURIER_BY_ID = "DELETE FROM couriers WHERE id = ?;"
DELETE_ORDER_BY_ID = "DELETE FROM orders WHERE Id = ?;"


def connect():
    return sqlite3.connect("data/data.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_PRODUCTS_TABLE)
        connection.execute(CREATE_COURIERS_TABLE)
        connection.execute(CREATE_ORDERS_TABLE)
        connection.execute(CREATE_ORDER_STATUS_TABLE)

def add_courier(connection, name, phone):
    with connection:
        connection.execute(INSERT_COURIER, (name, phone))

def add_product(connection, name, price):
    with connection:
        connection.execute(INSERT_PRODUCT, (name, price))

def add_order_status(connection, order_status):
    with connection:
        connection.execute(INSERT_ORDER_STATUS,(order_status,))

def add_order(connection,customer_name,customer_address,customer_phone,courier,status,items):
    with connection:
        connection.execute(INSERT_ORDER, (customer_name,customer_address,customer_phone,courier,status,items))

def update_product(connection,new_name,name_price,id):
    with connection:
        connection.execute(UPDATE_PRODUCT, (new_name,name_price,id))

def update_courier(connection,new_name,new_phone,id):
    with connection:
        connection.execute(UPDATE_COURIER, (new_name,new_phone,id))

def update_order(connection,new_customer_name,new_customer_address,
    new_customer_phone,courier,items, id):
    with connection:
        connection.execute(UPDATE_ORDER,(new_customer_name,
            new_customer_address,new_customer_phone,courier,items, id))

def update_order_status(connection, new_status, id):
    with connection:
        connection.execute(UPDATE_ORDER_STATUS, (new_status,id))

def get_all_products(connection):
    with connection:
        return connection.execute(GET_ALL_PRODUCTS).fetchall()

def get_all_couriers(connection):
    with connection:
        return connection.execute(GET_ALL_COURIERS).fetchall()

def get_all_orders(connection):
    with connection:
        return connection.execute(GET_ALL_ORDERS).fetchall()

def get_all_orders_status(connection):
    with connection:
        return connection.execute(GET_ALL_ORDER_STATUS).fetchall()


def get_products_by_name(connection, name):
    with connection:
        return connection.execute(GET_PRODUCTS_BY_NAME, (name,)).fetchall()

def get_products_by_id(connection, name):
    with connection:
        return connection.execute(GET_PRODUCTS_BY_ID, (name,)).fetchall()
def get_couriers_by_id(connection, name):
    with connection:
        return connection.execute(GET_COURIERS_BY_ID, (name,)).fetchall()

def get_orders_by_id(connection, name):
    with connection:
        return connection.execute(GET_ORDERS_BY_ID, (name,)).fetchall()

def get_products_by_price(connection):
    with connection:
        return connection.execute(GET_PRODUCTS_BY_PRICE).fetchall()

def delete_product(connection, name):
    with connection:
        connection.execute(DELETE_PRODUCT, (name,))

def delete_product_by_id(connection, id):
    with connection:
        connection.execute(DELETE_PRODUCT_BY_ID, (id,))

def delete_courier_by_id(connection, id):
    with connection:
        connection.execute(DELETE_COURIER_BY_ID, (id,))

def delete_order_by_id(connection, id):
    with connection:
        connection.execute(DELETE_ORDER_BY_ID, (id,))