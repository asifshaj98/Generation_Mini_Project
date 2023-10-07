import pytest
import sqlite3
from src.dbfunctions import display_orders, add_new_order, update_order, delete_order
from unittest.mock import patch
from unittest import mock

ALL_ORDERS = "SELECT * FROM orders"

@pytest.fixture
def setup_database():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''
	    CREATE TABLE orders
        (id integer PRIMARY KEY, 
        customer_name text,
        customer_address text,
        customer_phone text,
        courier integer,
        status integer,
        items text)''')
    sample_data = [
        (1, 'John', 'Unit 2, 12 Main Street, LONDON, WH1 2ER', '0789887334', 2, 1, '1,2,3'),
        (2, 'Timmy', 'Unit 2, 12 Main Street, LONDON, WH1 2ER', '0712345646', 3, 1, '2,4,6'),
        (3, 'Sheikh', 'Blue Street E1 123', '07969696969', 7, 3, '11,12,15')
    ]
    cursor.executemany('INSERT INTO orders VALUES(?, ?, ?, ?, ?, ?, ?)', sample_data)
    return connection


def test_connection(setup_database):

    cursor = setup_database
    assert len(list(cursor.execute(ALL_ORDERS))) == 3

@patch("src.dbfunctions.display_couriers")
@patch("src.dbfunctions.display_products_with_id")
@patch("builtins.input", side_effect = ["Numan","35 Numan Street","07123456","1,2,3",4])
def test_add_new_order(mock_input, mock_display_products_with_id, mock_display_courier, setup_database):
    cursor = setup_database

    assert len(list(cursor.execute(ALL_ORDERS))) == 3

    add_new_order(cursor)

    assert (4, 'Numan', '35 Numan Street', '07123456', 4, 1, "1,2,3") in cursor.execute(ALL_ORDERS)
    assert len(list(cursor.execute(ALL_ORDERS))) == 4
    
@patch("src.dbfunctions.display_couriers")
@patch("src.dbfunctions.display_products_with_id")
@patch("builtins.input", side_effect = ["1","Patrick","75 patty street","0712348238","3,1,2",4])
def test_update_orders(mock_input, mock_display_products_with_id, mock_display_courier, setup_database):
    cursor = setup_database

    assert (1, 'John', 'Unit 2, 12 Main Street, LONDON, WH1 2ER', '0789887334', 2, 1, '1,2,3') in cursor.execute(ALL_ORDERS)
    assert (1, 'Patrick', '75 patty street', '0712348238', 4, 1, '3,1,2') not in cursor.execute(ALL_ORDERS)
    
    update_order(cursor)

    assert (1, 'John', 'Unit 2, 12 Main Street, LONDON, WH1 2ER', '0789887334', 2, 1, '1,2,3') not in cursor.execute(ALL_ORDERS)
    assert (1, 'Patrick', '75 patty street', '0712348238', 4, 1, '3,1,2') in cursor.execute(ALL_ORDERS)

@patch("builtins.input", side_effect = ["1"])
def test_delete_order(mock_input, setup_database):
    cursor = setup_database

    assert (1, 'John', 'Unit 2, 12 Main Street, LONDON, WH1 2ER', '0789887334', 2, 1, '1,2,3') in cursor.execute(ALL_ORDERS)
    assert len(list(cursor.execute(ALL_ORDERS))) == 3

    delete_order(cursor)

    assert (1, 'John', 'Unit 2, 12 Main Street, LONDON, WH1 2ER', '0789887334', 2, 1, '1,2,3') not in cursor.execute(ALL_ORDERS)
    assert len(list(cursor.execute(ALL_ORDERS))) == 2