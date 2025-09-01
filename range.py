# The while loop iterates over and over again while the condition is true:
# The for loop and the range() function to iterate for a certain number of times:


for i in range(99, 0, -1):
    print(f"{i} bottles of beer on the wall")
    print(f"{i} bottles of beer")
    print("Take one down, pass it around")

# start = 99
# stop = 0 (but 0 is not included in the sequence)
# step = -1, so it decrements by 1 each time

for num in range(1, 100):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
