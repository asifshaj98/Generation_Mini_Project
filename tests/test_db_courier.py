import pytest
import sqlite3
from src.dbfunctions import display_couriers, add_new_courier, update_courier, delete_courier
from unittest.mock import patch
from unittest import mock

ALL_COURIERS = "SELECT * FROM couriers"

@pytest.fixture
def setup_database():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute('''
	    CREATE TABLE couriers
        (id integer PRIMARY KEY, name text, phone integer)''')
    sample_data = [
        (1, 'Sheikh', 97696969),
        (2, 'Patrick', 12345354),
        (3, 'Timmy', 7123456790),
        (4, 'Zoey', 7123456793),
        (5, 'Hannah', 7123456969),
        (6, 'Jenna', 7123456792)
    ]
    cursor.executemany('INSERT INTO couriers VALUES(?, ?, ?)', sample_data)
    return connection


def test_connection(setup_database):

    cursor = setup_database
    assert len(list(cursor.execute('SELECT * FROM couriers'))) == 6



@patch("builtins.input", side_effect = ["Carlton", 999])
def test_add_new_courier(mock_input, setup_database):
    cursor = setup_database

    assert len(list(cursor.execute(ALL_COURIERS))) == 6

    add_new_courier(cursor)

    assert (7, "Carlton", 999) in cursor.execute(ALL_COURIERS)
    assert len(list(cursor.execute(ALL_COURIERS))) == 7
    

@patch("builtins.input", side_effect = ["5","Patrick", 12345678])
def test_update_couriers(mock_input, setup_database):
    cursor = setup_database

    assert (5, 'Hannah', 7123456969) in cursor.execute(ALL_COURIERS)
    assert (5, "Patrick", 12345678) not in cursor.execute(ALL_COURIERS)
    
    update_courier(cursor)

    assert (5, 'Hannah', 7123456969) not in cursor.execute(ALL_COURIERS)
    assert (5, "Patrick", 12345678) in cursor.execute(ALL_COURIERS)

@patch("builtins.input", side_effect = ["6"])
def test_delete_courier(mock_input, setup_database):
    cursor = setup_database

    assert (6, 'Jenna', 7123456792) in cursor.execute(ALL_COURIERS)
    assert len(list(cursor.execute(ALL_COURIERS))) == 6

    delete_courier(cursor)

    assert (6, 'Jenna', 7123456792) not in cursor.execute(ALL_COURIERS)
    assert len(list(cursor.execute(ALL_COURIERS))) == 5