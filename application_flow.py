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
        print ("No order with this ID")
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


def sales_report(orders):
    num_of_orders = len(orders)
    closed_orders = []
    for order in orders:
        if order["status"] == "CLOSED":
            closed_orders.append(order)

    total_closed_orders =0
    for order in closed_orders:
        total_closed_orders += order["total"]
        
    sorted_closed_orders = sorted(closed_orders, key=lambda order: order["total"])
    most_expensive_order = sorted_closed_orders[-1]
    top_three_orders = sorted_closed_orders[-3:]
    show_sales_report(num_of_orders,total_closed_orders,most_expensive_order,top_three_orders)

  
def show_sales_report(num_of_orders,total_closed_orders,most_expensive_order,top_three_orders):
    print(f"""

---- SALES REPORT ----
NUMBER OF ORDERS: {num_of_orders}
TOTAL OF CLOSED ORDERS: {total_closed_orders}
MOST EXPENSIVE ORDER:\n{most_expensive_order}\n
TOP THREE ORDERES:
{top_three_orders[0]}\n
{top_three_orders[1]}\n
{top_three_orders[2]}

""")