# Mini Project Cafe CLI 
- A simple CLI application to track customer orders in a busy cafe.
## Project Background
- My client has launched a pop-up café in a busy business district. They are offering home-made lunches and refreshments to the surrounding offices. As such, they require a software application which helps them to log and track orders

## Client requirements
The client has given me these requirements for the app. 

- I want to maintain a collection of products and couriers.

- When a customer makes a new order, I need to create this on the
  system.

- I need to be able to update the status of an order i.e: preparing,
  out-for-delivery, delivered.

- When I exit my app, I need all data to be persisted and not lost.

- When I start my app, I need to load all persisted data.

- I need to be sure my app has been tested and proven to work well.

- I need to receive regular software updates

## Current Features
- Data persistence using SQlite3
- Unit and integration testing with pytest
- Implemented CRUD operations
• Create
• Read
• Update
• Delete

## Project Design
The project design was lead by the requirements of the client

```

├── data
│   ├── __init__.py
│   ├── couriers.csv
│   ├── data.db
│   ├── database.py
│   ├── orders.py
│   └── products.csv
├── src
│   ├── __init__.py
│   ├── dbfunctions.py
│   └── functions.py
├── tests
│   ├── __init__.py
│   ├── test_db_courier.py
│   ├── test_db_order.py
│   ├── test_db_product.py
│   └── test_menu.py
├── app.py
└── README.md

```

### Demo update order

```python

connection = database.connect()
database.create_tables(connection)

def update_order(connection):
    display_orders(connection)
    id = input("order id? ")
    order_id = database.get_orders_by_id(connection, id)
    for order in order_id:
        print(order)
    new_customer_name = input("New customer name? ")
    new_customer_address = input("New customer address? ")
    new_customer_phone = input("New customer phone number? ")
    display_products_with_id(connection)
    items = input("items? ")
    display_couriers(connection)
    couriers = input("New Courier index? ")
    if new_customer_name and new_customer_address and new_customer_phone:
        database.update_order(
            connection,
            new_customer_name,
            new_customer_address,
            new_customer_phone,
            couriers,
            items,
            id,
        )
    display_orders(connection)

```

#### Sql function to change the order by id

```python 

UPDATE_ORDER = """
UPDATE orders
SET customer_name = ?,
customer_address = ?,
customer_phone = ?,
courier = ?,
items = ?
WHERE id = ?;"""

def update_order(
    connection,
    new_customer_name,
    new_customer_address,
    new_customer_phone,
    courier,
    items,
    id,
):
    with connection:
        connection.execute(
            UPDATE_ORDER,
            (
                new_customer_name,
                new_customer_address,
                new_customer_phone,
                courier,
                items,
                id,
            ),
        )
```

### Test demo update order

```python 

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

@patch("src.dbfunctions.display_couriers")
@patch("src.dbfunctions.display_products_with_id")
@patch("builtins.input", side_effect = ["1","Patrick","75 patty street","0712348238","3,1,2",4])
def test_update_orders(mock_input, mock_display_products_with_id, mock_display_courier, setup_database):
    cursor = setup_database

    Johns_order = (1, 'John', 'Unit 2, 12 Main Street, LONDON, WH1 2ER', '0789887334', 2, 1, '1,2,3')
    Patricks_order = (1, 'Patrick', '75 patty street', '0712348238', 4, 1, '3,1,2')

    assert Johns_order in cursor.execute(ALL_ORDERS)
    assert Patricks_order not in cursor.execute(ALL_ORDERS)
    
    update_order(cursor)

    assert Johns_order not in cursor.execute(ALL_ORDERS)
    assert Patricks_order in cursor.execute(ALL_ORDERS)

```
![image](https://user-images.githubusercontent.com/115299269/203553121-fb36beb9-d4a2-4c73-967c-6a9610f08c9a.png)


## Meeting project requirements
- I used pytest to ensure core functionality
### Testing 
![image](https://user-images.githubusercontent.com/115299269/203553101-a932daf6-f714-4b39-aad9-166281118f7b.png)

## If you had more time, what is one thing you would improve upon?
- Compeleted the read me :)
- Make the prints formatted nicely
- Add error handling 
- Clean up the code, making it more presentable
- More test coverage
- Make my code changeable

## What did you most enjoy implementing?
- I enjoyed implementing the core functionality and seeing the program actually work


## Acknowledgments

* Carlton
* Patrick
* Numan & Nayan (testing dream team)
