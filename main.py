
def create_order():
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
    total_price = calculate_total_price(items)
    order = {"id":order_id,"items":items,"total":3,"status":"OPEN"}
    print (order)




def get_input(message):
    user_input = input (f"{message}")
    return user_input


create_order()

def calculate_price():
    pass
def calculate_discount():
    pass
def show_orders():
    pass



def calculate_total_price(items,products):
    total_price = 0
    for item in items:
        for product in products:
            if item ["product_id"] == product["id"]:
                total_price += product["price"] * item["quaantity"]
    price_after_sale = calculate_discount(total_price)
    return price_after_sale

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
