import json
import logging
logging.basicConfig(
    level=logging.INFO,                                  
    format="%(asctime)s %(levelname)s %(message)s",)
ORDER_FILE = "orders.json"

def load_orders_file():
    try:
        with open(ORDER_FILE, "r", encoding="utf-8") as file:
            orders =  json.load(file)
            
    except json.decoder.JSONDecodeError:
        print ("orders file empty, orders is an empty list")
        orders = []
    else:
        logging.info("loaded from order json file")
    return orders

def add_order_to_file(orders):
    try:
        with open(ORDER_FILE, "w", encoding="utf-8") as file:
            json.dump(orders, file, indent=2, ensure_ascii=False)

    except json.decoder.JSONDecodeError:
        print ("Un-able to add orders to file")
    else:
        logging.info("Updated order file with new orders")
