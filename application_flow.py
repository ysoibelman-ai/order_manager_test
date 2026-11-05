import logging
logging.basicConfig(
    level=logging.INFO,                                  
    format="%(asctime)s %(levelname)s %(message)s",)

def main_menu ():
    maain_menu_selection = input ("""

========== ORDER MANAGER ==========
Choose option:
1. Create order
2. Show all orders
3. Find order by ID
4. Close order
5. Show sales report
0. Exit
""")
    return maain_menu_selection

def get_input(message):
    user_input = input (f"{message}")
    logging.info(f"User entered {message}")
    return user_input

def show_orders(orders):
    logging.info("orders showed")
    print ("\n----ORDERS----")
    for order in orders:
        print (order)
    
def get_order_number(orders):
    if orders == []:
        return 1
    else:
        last_order = orders[-1]
        return last_order["id"]+1

def find_order_by_id(orders):
    logging.info("User searched for order by id")
    try:
        order_id = int(get_input("Enter order id: "))
    except ValueError:
        print ("id Needs to be a number")
        logging.warning("user entered invalid order id")
    else:
        for order in orders:
            if order_id == order["id"]:
                print (order)
                break
    finally:
        print ("\nReturning to main menu")


def close_order(orders):
    logging.info("user selected to close order by id")
    try:
        order_id = int(get_input("Enter order id to CLOSE: "))
    except ValueError:
        print ("id Needs to be a number")
        logging.warning("User entered invalid order id")
    else:
        for order in orders:
            if order_id == order["id"]:
                if  order["status"] == "OPEN":
                    order["status"] = "CLOSED"
                    print ('\nORDER CLOSED')
                    logging.info(f"user changed order {order_id} status to closed")
                    break
    finally:
        print ("\nReturning to main menu")