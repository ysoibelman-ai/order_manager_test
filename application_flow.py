from output import show_sales_report
import logging
logging.basicConfig(
    level=logging.INFO,                                  
    format="%(asctime)s %(levelname)s %(message)s",)



def get_input(message):
    user_input = input (f"{message}")
    return user_input

def get_order_number(orders):
    if orders == []:
        return 1
    else:
        last_order = orders[-1]
        return last_order["id"]+1

def find_order_by_id(orders):
    try:
        order_id = int(get_input("Enter order id: "))
    except ValueError:
        print ("id Needs to be a number")
        logging.warning("user entered invalid order id")
    else:
        for order in orders:
            if order_id == order["id"]:
                logging.info(f"User searched for order {order_id}")
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
                elif order["status"] == "CLOSED":
                    print ("\nOrder already closed\n")
    finally:
        print ("Returning to main menu\n")

def sales_report(orders):
    if orders == []:
        print ("NO ORDERS")
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