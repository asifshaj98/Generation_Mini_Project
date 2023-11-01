# Cafe-Order-application-Mini-Project :cake:

## Table of Contents
1. [Problem](#Problem)
2. [Objective](#Objective)
3. [Client's Requirement](#Clients-Requirement)
4. [Current Features](#current-features)
5. [File Structure](#file-structure)
6. [Ensuring the project requirements are met](#ensuring-the-project-requirements-are-met)
7. [Functionality Demo](#functionality-demo)
8. [Testing](#testing)
9. [Future Updates (Improvements)](#future-updatesimprovements-clock130)
10. [What I enjoyed implementing](#what-i-enjoyed-implementing)
11. [Dependencies](#dependencies)
12. [Installation](#installation)
13. [Timeline of the Project requirements](#timeline-of-the-project-requirements)

## Problem
A client has recently opened a pop-up café strategically located in a bustling business district. This café is geared towards offering delectable, homemade lunches, and refreshments to the busy professionals in nearby offices. To efficiently manage their growing customer base and streamline operations, the client is seeking a proficient software application. This application should enable the café to seamlessly log and track orders, enhancing their operational efficiency and providing exceptional service to their clientele. Data engineers are crucial in designing and implementing a robust, data-centric solution that can handle the influx of orders and ensure a smooth operational workflow for the café.
## Objective
The objective of this project is to develop a professional-grade software application tailored to assist a pop-up café in efficiently logging and tracking customer orders. The challenge is to design and implement a sophisticated Command-Line Interface (CLI) management system precisely catering to the specific needs and operations of a temporary café setup. The end goal is to enhance operational effectiveness, streamline order management, and elevate the overall customer experience within this dynamic and temporary cafe environment. Data engineers play a pivotal role in crafting a reliable, data-driven solution that optimizes order processing and facilitates seamless cafe operations.

## Client's Requirement
• Be able to maintain a collection of products and couriers.
• When a customer makes a new order, this order is created on the
    system.
• Be able to update the status of an order i.e: preparing,
out-for-delivery, delivered.
• When exiting the app, I need all data to be persisted and not lost.
• I need to be sure my app has been tested and proven to work well.
• I need to receive regular software updates.

## Current Features

    Manage the Products:
        -Show all the products
        -Add new product 
        -Delete a product
        -Update products
        -Save product list in csv format
        
        
    Manage the Orders:
        -Display orders details
        -Create orders
        -Update an existing order
        -Update order status
        -Delete orders
        -Save orders in csv format
        
    Manage the Couriers:
        -Show all couriers
        -Add new couriers
        -Update Couriers details
        -Delete Couriers
        -Save couriers in csv format
        
## File Structure
The project design was meticulously crafted based on the client's specific requirements. The file structure is organized to ensure modularity, maintainability, and ease of testing. The data directory holds essential data files and scripts to manage the project's database. The src directory contains the main application logic, encompassing database functions and other fundamental functionalities. The tests directory houses unit tests to validate the application's functionalities, promoting robustness and reliability. The app.py file is the entry point for the application, orchestrating the various components. The README.md file provides essential information and instructions for anyone interested in understanding and contributing to the project.
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
## Ensuring the project requirements are met.
In each subsequent week,additional requirements were given in order to achieve the specification laid out by the client.The end of this README is a weakly breakdown of the requirements.

By being flexible at the start of the program build was essential to allow additional requirements to be easily implemented. As the client's needs changed, the code had to adapt to these changes and as a result the code had to be refractored which included adding and rewriting functions.To check if the requirements were fulfilled, I began using unit test for the core functionality of the application.
### Importing Unittest
```python
from unittest import mock
import pytest
```

## Functionality Demo:
#### Update Order Function:
This code defines a function, update_order, that allows updating an existing order for a pop-up cafe management system. The user provides a new customer's name, address, phone number, selected items, and courier for the order. The function displays the current orders, prompts for an order ID, shows the order details, and updates the order with the new information. Finally, it displays the updated list of orders.
```python
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
        database.update_order(connection,new_customer_name,new_customer_address,
        new_customer_phone,couriers,items, id)
    display_orders(connection)
```

## Testing:
Testing code in a Cafe CLI application using frameworks like pytest and unittest is crucial for ensuring its reliability, functionality, and maintainability. These testing frameworks provide structured and systematic approaches to validate various components of the code. Testing helps uncover potential bugs, errors, or unexpected behavior in the codebase, allowing for timely and effective bug fixes. It also ensures that new features or modifications to existing ones don't inadvertently break the application. Moreover, through automated tests, developers can efficiently verify multiple functionalities, saving time and effort during development. Overall, testing with frameworks like pytest and unittest promotes confidence in the code's correctness and robustness, contributing to the delivery of a high-quality Cafe 
## Update 01/11/2023: Implementing CI/CD using Github Actions
The provided YAML file is a configuration file for GitHub Actions, a tool for implementing Continuous Integration (CI) and Continuous Deployment (CD) in your software development project. In this specific case, it's designed for the mini cafe project described earlier, which aims to enhance the operational efficiency of a pop-up cafe by developing a software application to log and track customer orders.
```bash
name: CI
on:
  push:
  pull_request:

jobs:
  run-tests:
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest]
        python-versions: ["3.11"]  # Use the latest Python version

    name: Test
    runs-on: ${{matrix.os}}

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v2  # Use a specific version to ensure the latest Python version is used
        with:
          python-version: ${{matrix.python-versions}}

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest
```
This YAML file configures GitHub Actions to automatically run tests on the project whenever there is a push to the repository or a pull request. This is an important aspect of CI/CD, as it helps ensure that any code changes do not introduce new bugs or issues and maintain the quality and reliability of the software application. For the mini cafe project, this CI process is crucial in ensuring that the software application designed for order logging and tracking works as expected, ultimately enhancing the operational efficiency and customer experience of the pop-up cafe.

#### Testing updating Courier:
```python
@patch("builtins.input", side_effect = ["5","Patrick", 12345678])
def test_update_couriers(mock_input, setup_database):
    cursor = setup_database

    assert (5, 'Hannah', 7123456969) in cursor.execute(ALL_COURIERS)
    assert (5, "Patrick", 12345678) not in cursor.execute(ALL_COURIERS)
    
    update_courier(cursor)

    assert (5, 'Hannah', 7123456969) not in cursor.execute(ALL_COURIERS)
    assert (5, "Patrick", 12345678) in cursor.execute(ALL_COURIERS)
```
#### Testing Adding New Order:
This function tests adding a new order in a cafe management system. It first checks the initial number of orders in the system, then calls the add_new_order function, and finally verifies that the new order is correctly added and the total number of orders has increased. The @patch decorators simulate user input and display functions for testing purposes.
```python
def test_add_new_order(mock_input, mock_display_products_with_id, mock_display_courier, setup_database):
    cursor = setup_database

    assert len(list(cursor.execute(ALL_ORDERS))) == 3

    add_new_order(cursor)

    assert (4, 'Numan', '35 Numan Street', '07123456', 4, 1, "1,2,3") in cursor.execute(ALL_ORDERS)
    assert len(list(cursor.execute(ALL_ORDERS))) == 4
    
@patch("src.dbfunctions.display_couriers")
@patch("src.dbfunctions.display_products_with_id")
@patch("builtins.input", side_effect = ["1","Patrick","75 patty street","0712348238","3,1,2",4])
```

#### Testing deleting New Product:
```python
@patch("builtins.input", side_effect = ["5"])
def test_delete_product(mock_input, setup_database):
    cursor = setup_database

    assert (5, "Milk", 2.0) in cursor.execute(ALL_PRODUCTS)
    assert len(list(cursor.execute(ALL_PRODUCTS))) == 7

    delete_product(cursor)

    assert (5, "Milk", 2.0) not in cursor.execute(ALL_PRODUCTS)
    assert len(list(cursor.execute(ALL_PRODUCTS))) == 6
```

## Future Updates(improvements) :clock130:
A modification I would implement to this program is to implement more error handling using try and except.This would dramatically reduce the chances of the program of terminating at crucial stages. Due to time constraints and the late addition of testing, I therefore avoided implementing this through out the program.
### Example:
```python
while True:
    try:
        Courier_num = int(input("Enter an integer: "))
    except ValueError:
        print("Please, enter a valid integer")
        continue
    else:
        print(f'You entered: {integer}')
        break
```

###
Towards the latter stages of the project, it became clear that writing tests for the code after the fact was very time consuming and required a lot of extra time and effort. This is something that, in the long run, can lead to difficulties in refactoring the code and making it easier for new members of a team who are not previously familiar with the project and the code.This is known as technical debt and this is not ideal in real world projects.To reduce this, the solution wpuld be to use test-driven development(TDD).Reflecting on his project, I would of liked to have more tests built into the code that would focus on different paths and analyse each scenarios.


## What I enjoyed implementing
I really enjoyed implementing testing in my project as it took me a long time.I am also proud of implementing OOP into the program as I struggled to grasp the concept of OOP.
To Conclude,I Enjoyed implementing all the skills we learnt in during the weeks at to eventally put them into pracice which increased my confidence with python programming

## Dependencies
- Python 3.10.7+

# Installation :exclamation:
```
git clone https://github.com/asifshaj98/Generation_Mini_Project.git
```


# Timeline of the Project requirements:

<details>
<summary>Week 1</summary>
<br>
As a user I want to:
<ul>
<li>create a product and add it to a list</li>
<li>view all products</li>
<li>STRETCH update or delete a product</li>
<br>
<li>A product should just be a string containing its name, i.e: "Coke Zero"</li>
<li>A list of products should be a list of strings , i.e: ["Coke Zero"]</li>
</ul>
</details>
<br>
<details>
<summary>Week 2</summary>
<br>
As a user I want to:
<ul>
<li>create a product or order and add it to a list</li>
<li>view all products or orders</li>
<li>STRETCH I want to be able to update or delete a product or order</li>
<br>
<li>A product should just be a string containing its name, i.e: "Coke Zero"</li>
<li>A list of products should be a list of strings, i.e: ["Coke Zero"]</li>
<li>An order should be a dict, i.e:</li>

```python
{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "status": "preparing"
}
```

<li>A list of orders should be a list of dicts, i.e: [{...}.{...}]</li>
</ul>
</details>
<br>
<details>
<summary>Week 3</summary>
<br>
As a user I want to:
<ul>
<li>create a product, courier, or order and add it to a list</li>
<li>view all products, couriers, or orders</li>
<li>update the status of an order</li>
<li>persist my data (products and couriers)</li>
<li>STRETCH update or delete a product, order, or courier</li>
<br>
<li>A product should just be a string containing its name, i.e: "Coke Zero"</li>
<li>A list of products should be a list of strings, i.e: ["Coke Zero"]</li>
<li>A courier should just be a string containing its name, i.e: "John"</li>
<li>A list of couriers should be a list of strings, i.e: ["John"]</li>
<li>An order should be a dict, i.e:</li>

```python
{
  "customer_name": "John",
  "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
  "customer_phone": "0789887334",
  "courier": 2,
  "status": "preparing"
}
```

<li>A list of orders should be a list of dicts, i.e: [{...}.{...}]</li>
<li>Data should be persisted to a .txt file on a new line for each courier or product, ie:</li>

```
John
Claire
```

</ul>
</details>
<br>
<details>
<summary>Week 4</summary>
<br>
As a user I want to:
<ul>
<li>create a product, courier, or order dictionary and add it to a list</li>
<li>view all products, couriers, or orders</li>
<li>update the status of an order</li>
<li>persist my data</li>
<li>STRETCH update or delete a product, order, or courier</li>
<li>BONUS list orders by status or courier</li>
<br>
<li>A product should be a dict, i.e:</li>

```python
{
"name": "Coke Zero",
"price": 0.8 # Float
}
```

<li>A courier should be a dict, i.e:</li>

```python
{
"name": "Bob",
"phone": "0789887889"
}
```

<li>An order should be a dict, i.e:</li>

```python
{
"customer_name": "John",
"customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
"customer_phone": "0789887334",
"courier": 2, # Courier index
"status": "preparing",
"items": "1, 3, 4" # Product index
}
```

<li>Data should be persisted to a .csv file on a new line for each courier, order, or product, ie:</li>

```csv
John,"Unit 2, 12 Main Street, LONDON, WH1 2ER",2,preparing,"1,3,4"
```

</ul>
</details>
<br>
<details>
<summary>Week 5</summary>
<br>
As a user I want to:
<ul>
<li>create a product or courier and add it to a database table</li>
<li>create an order and add the order dictionary to a list</li>
<li>view all products, couriers, or orders</li>
<li>update the status of an order</li>
<li>persist my data</li>
<li>STRETCH update or delete a product, order, or courier</li>
<li>BONUS list orders by status or courier</li>
<li>BONUS track my product inventory</li>
<li>BONUS import/export my entities in CSV format</li>
<br>
<li>A row in the products table should contain the following information:</li>

```python
{
 "id": 4,
 "name": "Coke Zero",
 "price": 0.8
}
```

<li>A row in the couriers table should contain the following information:</li>

```python
{
 "id": 2,
 "name": "Bob",
 "phone": "0789887889"
}
```

<li>An order should be a dict, i.e:</li>

```python
{
 "customer_name": "John",
 "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
 "customer_phone": "0789887334",
 "courier": 2, # Courier ID
 "status": "preparing",
 "items": "1, 3, 4" # Product IDs
}
```

<li>Orders should be persisted to a .csv file on a new line for each order, ie:</li>

```csv
John,"Unit 2, 12 Main Street, LONDON, WH1 2ER",2,preparing,"1,3,4"
```

