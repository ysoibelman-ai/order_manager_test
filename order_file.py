from application_flow import get_input
from output import show_order_summary
from validations import check_valid_product_id,check_valid_product_quantity
import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s",)

def create_order(products,orders,order_number):
    order_id = order_number
    items = []
    while True:
        order_menu = input(f"Enter 1 to add product, 0 to finish order: ")
        match order_menu:
            
            case "1":
                while True:
                    try:
                        product_id = int(get_input("enter product id: "))
                    except ValueError:
                        print ("id needs to be a number")
                        logging.warning("user entered invalid id")
                        continue
                    else:
                        if not check_valid_product_id(product_id):
                            print ("id must be a number from 1 to 5")
                            continue
                        break
                while True:
                    try:
                        product_quantity =int(get_input("enter product quantity: "))
                    except ValueError:
                        print ("quantity must be a number")
                        logging.warning("user entered invalid quantity")
                        continue
                    else:
                        if not check_valid_product_quantity(product_quantity):
                            print("quantity must be a positive number")
                            continue
                        break

                product = {"product_id":product_id,"quantity":product_quantity}
                items.append(product)

            case "0":
                break
            case _:
                print ("invalid 'ENTER' returning to menu")
                logging.warning("user selected invalid menu option")

    price_before_discount,discount,price_after_discount = calculate_total_order_price(items,products)
    order = {"id":order_id,"items":items,"total":price_after_discount,"status":"OPEN"}
    orders.append(order)
    show_order_summary(price_before_discount,discount,price_after_discount)

def calculate_total_order_price(items,products):
    total_price = 0
    for item in items:
        for product in products:
            if item ["product_id"] == product["id"]:
                total_price += product["price"] * item["quantity"]
    discount,price_after_discount = calculate_order_discount(total_price)
    return total_price,discount,price_after_discount

def calculate_order_discount(total_price):
    if total_price < 300:
        price_after_discount = total_price
        return "No Discount",price_after_discount
    
    elif 300 <= total_price < 700:
        price_after_discount = total_price * 0.95
        return "5%",price_after_discount
    
    elif 700 <= total_price <1500:
        price_after_discount = total_price * 0.9
        return "10%",price_after_discount
    
    elif total_price >= 1500:
        price_after_discount = total_price * 0.85
        return "15%",price_after_discount