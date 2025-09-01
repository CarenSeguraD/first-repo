import random

while True:
    read_the_cap = int(input(
        "Oh a Snapple bottle randomly appeared 🤯\nWhat should we do?\n1. Drink the Snapple and check the bottle cap for a random fact.\n2. Ignore bottle and move on with my day."))
    read_the_cap_2 = int(input(
        "Damn I was thirsty as fuck, that drink was nice! what does this cap says?\n1. Read the cap\n2. Don't mind the message"))

    if read_the_cap == 1:
        print(read_the_cap_2)
        if read_the_cap_2 == 1:
            random_message = random.randint(0, 5)

            if random_message == 0:
                print('Flamingos turn pink from eating shrimp.')
                break
            elif random_message == 1:
                print('The only food that doesn\'t spoil is honey.')
                break
            elif random_message == 2:
                print('Shrimp can only swim backwards.')
                break
            elif random_message == 3:
                print('A taste bud\'s life span is about 10 days.')
                break
            elif random_message == 4:
                print('It is impossible to sneeze while sleeping.')
                break
            else:
                print('It is illegal to sing off-key in North Carolina.')
                break
        elif read_the_cap_2 == 2:
            print("Aqui no andamo en gente manito *throws the bottle cap out*")
            break
    else:
        print("Na this look sus *walks away*")
        break
