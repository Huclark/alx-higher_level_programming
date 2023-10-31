#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit

print(f"Last digit of {number:d} is {last_digit:d}", end=" ")

if last_digit > 5:
    print(f"and is greater than 5")

elif last_digit == 0:
    print(f"and is 0")

elif last_digit < 6 and last_digit != 0:
    print(f"and is less than 6 and not 0")
