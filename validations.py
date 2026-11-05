import logging
logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s",)

def check_valid_product_id(id):
    if id in [1,2,3,4,5]:
        return True
    logging.warning("invalid product id entered")
    return False

def check_valid_product_quantity(product_quantity):
    if product_quantity > 0:
        return True
    else:
        logging.warning("invalid product quantity entered")
        return False