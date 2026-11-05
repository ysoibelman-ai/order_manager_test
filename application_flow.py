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
    return maain_menu_selection

def get_input(message):
    user_input = input (f"{message}")
    return user_input