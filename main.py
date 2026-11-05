from order_file import create_order
from application_flow import main_menu

def main ():
    orders = []
    products = [
        {"id": 1, "name": "Keyboard", "price": 120},
        {"id": 2, "name": "Mouse", "price": 80},
        {"id": 3, "name": "Monitor", "price": 900},
        {"id": 4, "name": "Headphones", "price": 200},
        {"id": 5, "name": "USB Cable", "price": 30}]

    while True:
        main_menu_selection = main_menu()
        match main_menu_selection:
            case "1":
                create_order(products,orders)
            case "2":
                            pass
            case "3":
                             pass
            case "4":
                             pass
            case "5":
                    pass
            case "0":
                    exit()
            case _:
                    print(f"\n INVALID INPUT TRY AGAIN:")

if __name__ == "__main__":
        main()
def calculate_price():
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
