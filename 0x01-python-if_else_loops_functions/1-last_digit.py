#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    last_dig = abs(number) % 10

elif number < 0:
    last_dig = -(abs(-number) % 10)

if last_dig == 0:
    print(f"Last digit of {number} is 0 and is 0")

elif last_dig < 6:
    print(f"Last digit of {number} is {last_dig} and is less than 6 and not 0")

else:
    print(f"Last digit of {number} is {last_dig} is greater than 5")
