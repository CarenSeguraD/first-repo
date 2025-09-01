House = {"Gryffindor": 0, "Ravenclaw": 0, "Hufflepuff": 0, "Slytherin": 0}

question_1 = int(
    input("Q1) Do you like Dawn or Dusk? \n1) Dawn\n2) Dusk\nSelect an option:"))
if question_1 == 1:
    House["Gryffindor"] += 1
    House["Ravenclaw"] += 1
elif question_1 == 2:
    House["Hufflepuff"] += 1
    House["Slytherin"] += 1
else:
    print("Wrong input.")

question_2 = int(input(
    "Q2) When I\’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\nSelect an option:"))
if question_2 == 1:
    House["Hufflepuff"] += 2
elif question_2 == 2:
    House["Slytherin"] += 2
elif question_2 == 3:
    House["Ravenclaw"] += 2
elif question_2 == 4:
    House["Gryffindor"] += 2
else:
    print("Wrong input.")

question_3 = int(input(
    "Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\nSelect an option:"))
if question_3 == 1:
    House["Hufflepuff"] += 4
elif question_3 == 2:
    House["Slytherin"] += 4
elif question_3 == 3:
    House["Ravenclaw"] += 4
elif question_3 == 4:
    House["Gryffindor"] += 4
else:
    print("Wrong input.")


top_house = max(House, key=House.get)
print(f"House with the most points is!: {top_house}")
