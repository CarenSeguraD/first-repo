from random import choice as ch
from math import pi

print("")

planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Saturn'
]


def radius(r):
    return 4 * pi * r**2


random_planet = ch(planets)

if random_planet == 'Mercury':
    print(
        f"You landed on {random_planet}. Its radius is {round(radius(2440))}.")
elif random_planet == 'Venus':
    print(
        f"You landed on {random_planet}. Its radius is {round(radius(6052))}")
elif random_planet == 'Earth':
    print(
        f"You landed on {random_planet}. Its radius is {round(radius(6371))}")
elif random_planet == 'Mars':
    print(
        f"You landed on {random_planet}. Its radius is {round(radius(3390))}")
elif random_planet == 'Saturn':
    print(
        f"You landed on {random_planet}. Its radius is {round(radius(58232))}")
else:
    print("Oops! An error occurred.")
