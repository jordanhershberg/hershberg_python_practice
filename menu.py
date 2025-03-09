# 5) menu
menu = {"pizza": 1.99, "soda": 0.69, "WINGSTOP TRIPLE CHOCOLATE CHUNK COOKIE": 2.49}

def add_to_menu(item, price):
    menu[item] = price

add_to_menu("hot dog", 1.50)
print(menu)