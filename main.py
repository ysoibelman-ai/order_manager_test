

def main ():
    while True:
        main_menu_selection = main_menu()



        break
    
    pass


def create_order():
    order_id = int(get_input("enter order id: "))
    items = []
    products = [
    {"id": 1, "name": "Keyboard", "price": 120},
    {"id": 2, "name": "Mouse", "price": 80},
    {"id": 3, "name": "Monitor", "price": 900},
    {"id": 4, "name": "Headphones", "price": 200},
    {"id": 5, "name": "USB Cable", "price": 30}]
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
    total_price = calculate_total_price(items,products)
    order = {"id":order_id,"items":items,"total":total_price,"status":"OPEN"}
    print (order)

def calculate_total_price(items,products):
    total_price = 0
    for item in items:
        for product in products:
            if item ["product_id"] == product["id"]:
                total_price += product["price"] * item["quantity"]
    price_after_sale = calculate_discount(total_price)
    return price_after_sale

def calculate_discount(total_price):
    if total_price < 300:
        return total_price
    elif 300 <= total_price < 700:
        return total_price * 0.95
    elif 700 <= total_price <1500:
        return total_price * 0.9
    elif total_price >= 1500:
        return total_price * 0.85



def get_input(message):
    user_input = input (f"{message}")
    return user_input


create_order()

def calculate_price():
    pass

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

    pass
def show_orders():
    pass




"""
products = [
    {"id": 1, "name": "Keyboard", "price": 120},
    {"id": 2, "name": "Mouse", "price": 80},
    {"id": 3, "name": "Monitor", "price": 900},
    {"id": 4, "name": "Headphones", "price": 200},
    {"id": 5, "name": "USB Cable", "price": 30}
]
מבנה הזמנה לדוגמה (הסכום לאחר הנחה):
order = {
    "id": 1,
    "items": [{"product_id": 1, "quantity": 2},
              {"product_id": 3, "quantity": 1}],
    "total": 1026.0,
    "status": "OPEN"
}
""" 


"""
order = {
    "id": 1,
    "items": [{"product_id": 1, "quantity": 2},
              {"product_id": 3, "quantity": 1}],
    "total": 1026.0,
    "status": "OPEN"
}
"""
