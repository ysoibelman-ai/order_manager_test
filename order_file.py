from application_flow import get_input

def create_order(products,orders):
    print (orders)
    order_id = int(get_input("enter order id: "))
    items = []
   
    while True:
        order_menu = input(f"Enter 1 to add product, 0 to finish order: ")
        match order_menu:
            
            case "1":
                product_id = order_id = int(get_input("enter product id: "))
                product_quantity =int(get_input("enter product quantity: "))
                product = {"product_id":product_id,"quantity":product_quantity}
                items.append(product)

            case "0":
                break
            case _:
                print ("invalid 'ENTER' returning to menu")
    total_price = calculate_total_order_price(items,products)
    order = {"id":order_id,"items":items,"total":total_price,"status":"OPEN"}
    orders.append(order)

def calculate_total_order_price(items,products):
    total_price = 0
    for item in items:
        for product in products:
            if item ["product_id"] == product["id"]:
                total_price += product["price"] * item["quantity"]
    price_after_sale = calculate_order_discount(total_price)
    return price_after_sale

def calculate_order_discount(total_price):
    if total_price < 300:
        return total_price
    elif 300 <= total_price < 700:
        return total_price * 0.95
    elif 700 <= total_price <1500:
        return total_price * 0.9
    elif total_price >= 1500:
        return total_price * 0.85

    
