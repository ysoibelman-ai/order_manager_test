import logging
logging.basicConfig(
    level=logging.INFO,                                  
    format="%(asctime)s %(levelname)s %(message)s",)

def main_menu ():
    main_menu_selection = input ("""
========== ORDER MANAGER ==========
Choose option:
1. Create order
2. Show all orders
3. Find order by ID
4. Close order
5. Show sales report
0. Exit
""")
    return main_menu_selection

def show_orders(orders):
    logging.info("orders showed")
    print ("\n----ORDERS----")
    for order in orders:
        print (order)

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

def show_order_summary(price_before_discount,discount,price_after_discount):
    print (f"\nORDER SUMMARY\nPrice b4 discount: {price_before_discount}\nDiscount: {discount}\nPrice after discount: {price_after_discount}")