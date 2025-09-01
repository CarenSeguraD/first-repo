number = int(input("Type any number: "))
total = 0

for i in range(1, number + 1):
    total += i * i

print(total)

# range(start, stop)
# start is inclusive (the loop begins at this value).
# stop is exclusive (the loop ends just before this value).
# Because range stops at stop - 1, setting stop = n + 1 makes sure n is included.

# -Iteration 1 (i = 1):
# total = 0 + (1 * 1) = 1
# -Iteration 2 (i = 2):
# total = 1 + (2 * 2) = 5
# -Iteration 3 (i = 3):
# total = 5 + (3 * 3) = 14
# So by the end of the loop, total equals 14, which is 1** + 2** + 3**.
