bills = [13.99, 28.75, 9.99, 9.99, 6.95, 7.45, 16.45, 16.45]
total = 0

for bill in bills:
    total += bill
per_person = total / 4
print(f"Total bill per person: ${per_person}")
