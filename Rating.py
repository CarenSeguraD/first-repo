print("*********************************")
print("*           Rate Us             *")
print("*********************************")
print("                                 ")

rating = float(input("How would you rate this restaurant?"))

if rating > 4.5:
    print("Extraordinar\n⭐️⭐️⭐️⭐️⭐️")
elif rating >= 4:
    print("Excellent\n⭐️⭐️⭐️⭐️")
elif rating >= 3:
    print("Good\n⭐️⭐️⭐️")
elif rating >= 2:
    print("Fair\n⭐️⭐️")
else:
    print("Poor\n⭐️")
