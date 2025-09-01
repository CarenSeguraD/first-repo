current_animal_inventory = {"tigers": 5, "bears": 3, "deers": 10}


print("**********************HOLY'S ZOO***********************")
print(" ")
print(' ')
while True:
    user_interface = int(
        input("Select 1 to know your current inventory\nSelect 2 to add an animal\nSelect 3 to exit"))
    if user_interface == 1:
        format_list = str(current_animal_inventory)[1:-1]
        print(format_list)
    elif user_interface == 2:
        add_animal = input("Please provide animal name:")
        count = input(f"Please provide the amount of incoming {add_animal}'s")
        current_animal_inventory.update({add_animal: count})
        print("Updated list", current_animal_inventory)
    elif user_interface == 3:
        break
    else:
        print("Wrong input")
