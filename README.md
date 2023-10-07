# Cafe-Order-application-Mini-Project :cake:
## Problem
A client has launched a pop-up café in a busy business district.The cafe is offering home-made lunches and refreshments to the surrounding offices.Hence, they require a software application which helps them to log and track orders.
## Objective
Creating a software application that helps a pop-up café log and track orders.The aim of this project is to create a CLI management system designed for a pop up cafe.

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
        
## Project design
The project was designed over a period of 6 weeks in which new features will be implemented as "software updates". To help with the overall interface of the program,pseudocodes were given each week to give a brief overview of the whole program.

To meet the design requirements, I began by creating the main menu function:
```python
def main_menu():
    os.system("cls")
    cmd_main_menu_ = int(input("""
    ************** Welcome to my CLI Cafe Project, Choose an options below ******************
                              ****MAIN MENU****
                                0: Exit
                                1: Product Menu   """))
   while True:
       if cmd_main_menu == 0:
             exit()
       elif cmd_main_menu == 1:
             product_Menu()
#This will be displayed on command line
```
This simple conditional statement checks if the user wants to exit or continue with the program. This functions forms the core structure of this program.

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
```python
def update_order(self):
        os.system("cls")
        temp_list = self.order_list
        for count, value in enumerate(self.order_list):
            print(count + 1, value)
        try:
            index_of_thing_to_update = int(input(f'Please pick an order to update: '))

            old_thing = copy.deepcopy(temp_list[index_of_thing_to_update - 1])
            new_thing = temp_list[index_of_thing_to_update - 1]
            for key in new_thing:
                new_key = input(f'What is the new {key}? ')
                if new_key == '':
                    pass
                else:
                    new_thing[key] = new_key

            temp_list[index_of_thing_to_update - 1] = new_thing

            print(f"\n'{old_thing}' is updated to '{new_thing}'\n")
            self.order_list = temp_list
            self.save_list_to_csv()

        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            self.update_order()
```



## Testing:
Apart from doing manuel testing to ensure the app meeting the requirements.
Some unit testings are also done.A total of10 Tests were made at this point of time.
One is used to test the save list to csv function. Two are used to test if the create product function will raise type error for unknown inputs and successfully append the item to the list.

```python
def test_product_menu_create_courier_raise_type_error():
    # Assembly
    courier_info = [{"name": "Test_Courier", "phone": "1834633"}]
    product_menu_under_test = FakeCourierMenu(courier_info)

    # Action / Assertion
    with pytest.raises(TypeError):
        product_menu_under_test.create_courier('Pepsi', 100)
```

```python
order_menu_under_test = FakeOrderMenu(orders)
assert order_menu_under_test.order_list[1]['status'] == 'PREPARING'

order_menu_under_test.update_order()

assert order_menu_under_test.order_list[1]['status'] == 'Delivered'
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
git clone https://github.com/asifshaj98/Cafe-Order-Tracking-application
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

