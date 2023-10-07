import src.functions as pf
from src.functions import Menu
import data.database as database
from src.dbfunctions import *

# pf.read_file()
# main_menu_input = Menu()

def uplink():
    connection = database.connect()
    database.create_tables(connection)

    main_menu_input = Menu()

    while True:
        if main_menu_input == "1":
            products_menu_input = Menu().products_menu()

            if products_menu_input == "0":
                print("Returning to Main Menu")
                main_menu_input = Menu().main_menu()

            elif products_menu_input == "1":
                display_products(connection)

            elif products_menu_input == "2":
                add_new_product(connection)

            elif products_menu_input == "3":
                update_product(connection)

            elif products_menu_input == "4":
                delete_product(connection)

        elif main_menu_input == "2":
            order_menu_input = Menu().order_menu()

            if order_menu_input == "0":
                print("Returning to Main Menu")
                main_menu_input = Menu().main_menu()
            
            elif order_menu_input == "1":
                display_orders(connection)
                    
            elif order_menu_input == "2":
                add_new_order(connection)

            elif order_menu_input == "3":
                update_order_status(connection)

            elif order_menu_input == "4":
                update_order(connection)

            elif order_menu_input == "5":
                delete_order(connection)

        elif main_menu_input == "3":
            courier_menu_input = Menu().courier_menu()

            if courier_menu_input == "0":
                print("Returning to Main Menu")
                main_menu_input = Menu().main_menu()

            elif courier_menu_input == "1":
                display_couriers(connection)

            elif courier_menu_input == "2":
                add_new_courier(connection)
            
            elif courier_menu_input == "3":
                update_courier(connection)
            
            elif courier_menu_input == "4":
                delete_courier(connection)

        elif main_menu_input == "0":
            print("""

   _____  ____   ____  _____    ______     ________         
  / ____|/ __ \ / __ \|  __ \  |  _ \ \   / |  ____|        
 | |  __| |  | | |  | | |  | | | |_) \ \_/ /| |__           
 | | |_ | |  | | |  | | |  | | |  _ < \   / |  __|          
 | |__| | |__| | |__| | |__| | | |_) | | |  | |____   _ _ _ 
  \_____|\____/ \____/|_____/  |____/  |_|  |______| (_(_(_)
                                                                                                                 
""")
            exit()
        else:
            print("Not a vaild input")
            main_menu_input = Menu().main_menu()
            
uplink()