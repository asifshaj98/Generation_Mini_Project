import data.database as database

def display_products(connection):
    products = database.get_all_products(connection)

    print("Product Information:")
    print("{:<20} {:<10}".format("Product", "Price ($)"))
    print("="*32)  # Line for separation

    for product in products:
        print("{:<20} ${:<10.2f}".format(product[1], product[2]))

def display_products_unchanged(connection):
    products = database.get_all_products(connection)

    for i in products:
        print(i)


def display_products_with_id(connection):
    products = database.get_all_products(connection)

    print("Product Information:")
    print("{:<5} {:<20} {:<10}".format("ID", "Product", "Price ($)"))
    print("="*37)  # Line for separation

    for product in products:
        print("{:<5} {:<20} ${:<10.2f}".format(product[0], product[1], product[2]))

def add_new_product(connection):
    name = input("Enter New Product Name: ")
    price = input("Enter New Product Price: ")
    if name and price:
        database.add_product(connection, name.title(), price)

def update_product(connection):
    display_products_with_id(connection)
    id = input("Product id? ")
    id_show = database.get_products_by_id(connection, id)
    for i in id_show:
        print(f"{i[1]} {i[2]:.2f}")
    new_name = input("Updated product name: ")
    new_price = input("Updated product price: ")
    if new_name and new_price:
        database.update_product(connection, new_name.title(), new_price, id)
    display_products(connection)

def delete_product(connection):
    display_products_with_id(connection)
    id = input("Product Id? ")
    id_show = database.get_products_by_id(connection, id)
    for i in id_show:
        print(f"{i[1]} {i[2]:.2f}")
    database.delete_product_by_id(connection, id)
    display_products(connection)


def display_couriers(connection):
    couriers = database.get_all_couriers(connection)

    print("Courier Information:")
    print("{:<5} {:<20} {:<15}".format("ID", "Name", "Phone"))
    print("="*40)  # Line for separation

    for courier in couriers:
        print("{:<5} {:<20} {:<15}".format(courier[0], courier[1], courier[2]))

def add_new_courier(connection):
    name = input("Enter New Courier Name: ")
    phone = input("Enter New Courier Phone Number: ")
    if name and phone:
        database.add_courier(connection, name.title(), phone)

def update_courier(connection):
    display_couriers(connection)
    id = input("Courier Id? ")
    courier_id = database.get_couriers_by_id(connection, id)
    for selected_courier in courier_id:
        print(selected_courier)
    new_name = input("Updated courier name: ")
    new_phone = input("Updated courier phone number: ")
    if new_name and new_phone:
        database.update_courier(connection, new_name.title(), new_phone, id)
    display_couriers(connection)

def delete_courier(connection):
    display_couriers(connection)
    id = input("Courier Id? ")
    id_show = database.get_couriers_by_id(connection, id)
    for selected_courier in id_show:
        print(selected_courier)
    database.delete_courier_by_id(connection, id)
    display_couriers(connection)

#*****************************************************

def display_orders(connection):
    orders = database.get_all_orders(connection)

    print("Order Information:")
    print("{:<5} {:<20} {:<40} {:<15} {:<10} {:<10}".format("ID", "Customer Name", "Customer Address", "Customer Phone", "Status", "Items"))
    print("="*105)  # Line for separation

    for order in orders:
        print('{:<5} {:<20} {:<40} {:<15} {:<10} {:<10}'.format(order[0], order[1], order[2], order[3], order[4], order[5]))

def display_order_status(connection):
    orders = database.get_all_orders_status(connection)
    for order in orders:
        print(order)

def add_new_order(connection):
    customer_name = input("New Customer Name? ")
    customer_address = input("New Customer Address? ")
    customer_phone = input("New Customer Phone number? ")
    display_products_with_id(connection)
    items = input("items? ")
    display_couriers(connection)
    couriers = input("Courier index? ")
    status = 1
    if customer_name and customer_address and customer_phone:
        database.add_order(connection, customer_name.title(),
        customer_address, customer_phone, couriers, status, items)
    display_orders(connection)

def update_order_status(connection):
    display_orders(connection)
    id = input("select order by id? ")
    selected_id = database.get_orders_by_id(connection, id)
    for i in selected_id:
        print(i)
    display_order_status(connection)
    new_status = input("new order status? ")
    database.update_order_status(connection, new_status, id)
    display_orders(connection)

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

def delete_order(connection):
    display_orders(connection)
    id = input("order id? ")
    order_id = database.get_orders_by_id(connection, id)
    for order in order_id:
        print(order)
    database.delete_order_by_id(connection, id)
    display_orders(connection)
