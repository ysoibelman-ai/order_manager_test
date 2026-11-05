from application_flow import get_input

def create_order(products,orders,order_number):
    print (orders)
    
    order_id = order_number
    items = []
   
    while True:
        order_menu = input(f"Enter 1 to add product, 0 to finish order: ")
        match order_menu:
            
            case "1":
                product_id = int(get_input("enter product id: "))
                product_quantity =int(get_input("enter product quantity: "))
                product = {"product_id":product_id,"quantity":product_quantity}
                items.append(product)

            case "0":
                break
            case _:
                print ("invalid 'ENTER' returning to menu")
    price_before_discount,discount,price_after_discount = calculate_total_order_price(items,products)
    
    print (f"\nORDER SUMMARY\nPrice b4 discount: {price_before_discount}\nDiscount: {discount}\nPrice after discount: {price_after_discount}")

    order = {"id":order_id,"items":items,"total":price_after_discount,"status":"OPEN"}
    orders.append(order)

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
        return total_price,"no_discount",price_after_discount
    
    elif 300 <= total_price < 700:
        price_after_discount = total_price * 0.95
        return "5%",price_after_discount
    
    elif 700 <= total_price <1500:
        price_after_discount = total_price * 0.9
        return "10%",price_after_discount
    
    elif total_price >= 1500:
        price_after_discount = total_price * 0.85
        return "15%",price_after_discount