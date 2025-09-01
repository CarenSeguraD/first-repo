
def welcome():
    print("Welcome to Holy's restaurant!\nDrive-Thru is on the left.")
    print(" ")
    print("+========== ✩MENU✩ =========+")
    print("|===========================|")
    print("| 0 - 🍔 Cheeseburger       |")
    print("| 1 - 🍟 Fries              |")
    print("| 2 - 🥤 Soda               |")
    print("| 3 - 🍦 Vanilla Ice Cream  |")
    print("| 4 - 🍪 Chocolate Cookies  |")
    print("+===========================+")
    print(" ")


def get_item(x):
    items = ['🍔 Cheeseburger', '🍟 Fries', '🥤 Soda',
             '🍦 Vanilla  Ice Cream', '🍪 Chocolate Cookies']
    order = int(
        input("What would you like to order?\nPlease enter the number: "))
    if order == 0:
        print(f"A {get_item(0)}, great choice! Your order will be ready soon.")
    elif order == 1:
        print(f"{get_item(1)}, hot and crispy! Your order will be ready soon.")
    elif order == 2:
        print(f"A refreshing {get_item(2)}! Your order will be ready soon.")
    elif order == 3:
        print(f"A creamy {get_item(3)}! Your order will be ready soon.")
    elif order == 4:
        print(f"Some delicious {get_item(4)}! Your order will be ready soon.")
    else:
        print("Sorry, ❌ please enter a number seen on the menu.")
