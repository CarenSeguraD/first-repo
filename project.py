import random
print("")
print("******************************************")
print("*(ﾉ ◕ ヮ ◕)ﾉ*:･ﾟ ✧ Welcome to the game! *")
print("******************************************")
print("")
print("==========Rock, Paper, Scissors===========")
print("")

player = int(input(
    "Choose your weapon:\n1. R✊ck\n2. P✋per\n3. Sc✌️ssors\n\nEnter your choice: "))
computer = random.randint(1, 3)

if player == 1 and computer == 1:
    print("It's a tie! Both chose Rock.")
elif player == 1 and computer == 2:
    print("You lose! Rock vs Paper.")
elif player == 1 and computer == 3:
    print("You win! Rock vs Scissors.")
elif player == 2 and computer == 1:
    print("You win! Paper vs Rock.")
elif player == 2 and computer == 2:
    print("It's a tie! Both chose Paper.")
elif player == 2 and computer == 3:
    print("You lose! Paper vs Scissors.")
elif player == 3 and computer == 1:
    print("You lose! Scissors vs Rock.")
elif player == 3 and computer == 2:
    print("You win! Scissors vs Paper.")
elif player == 3 and computer == 3:
    print("It's a tie! Both chose Scissors.")
else:
    print("Invalid choice! Please select 1, 2, or 3.")
