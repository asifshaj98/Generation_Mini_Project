import pytest
import sqlite3
from src.dbfunctions import display_products_unchanged, add_new_product,update_product, delete_product
from unittest.mock import patch
from unittest import mock

ALL_PRODUCTS = "SELECT * FROM products"

@pytest.fixture
def setup_database():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''
	    CREATE TABLE products
        (id integer PRIMARY KEY, name text, price float)''')
    sample_data = [
        (1, 'Redbull', 2.15),
        (2, 'Tea', 1.40),
        (3, 'Coffee', 2.40),
        (4, 'Water', 1.5),
        (5, 'Milk', 2.0),
        (6, 'Watermelon', 8.0),
        (7, 'Cookies', 1.0)
    ]
    cursor.executemany('INSERT INTO products VALUES(?, ?, ?)', sample_data)
    return connection


def test_connection(setup_database):

    cursor = setup_database
    assert len(list(cursor.execute('SELECT * FROM products'))) == 7

@patch("builtins.print")
def test_display_products_unchanged(mock_print,setup_database):

    cursor = setup_database
    display_products_unchanged(cursor)
    mock_print.assert_called_with((7, 'Cookies', 1.0))

@patch("builtins.input", side_effect = ["Iron Brew", 0.75])
def test_add_new_product(mock_input, setup_database):
    cursor = setup_database

    assert len(list(cursor.execute(ALL_PRODUCTS))) == 7

    add_new_product(cursor)

    assert (8, "Iron Brew", 0.75) in cursor.execute(ALL_PRODUCTS)
    assert len(list(cursor.execute(ALL_PRODUCTS))) == 8
    

@patch("builtins.input", side_effect = ["5","Pepsi Max", 1.40])
def test_update_products(mock_input, setup_database):
    cursor = setup_database

    assert (5, "Milk", 2.0) in cursor.execute(ALL_PRODUCTS)
    assert (5, "Pepsi Max", 1.40) not in cursor.execute(ALL_PRODUCTS)
    
    update_product(cursor)

    assert (5, "Milk", 2.0) not in cursor.execute(ALL_PRODUCTS)
    assert (5, "Pepsi Max", 1.40) in cursor.execute(ALL_PRODUCTS)

@patch("builtins.input", side_effect = ["5"])
def test_delete_product(mock_input, setup_database):
    cursor = setup_database

    assert (5, "Milk", 2.0) in cursor.execute(ALL_PRODUCTS)
    assert len(list(cursor.execute(ALL_PRODUCTS))) == 7

    delete_product(cursor)

    assert (5, "Milk", 2.0) not in cursor.execute(ALL_PRODUCTS)
    assert len(list(cursor.execute(ALL_PRODUCTS))) == 6







    