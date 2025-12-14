#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
flag = 0
last = 0
if number >= 0:
    flag = 1
    last = (number % 10)
else:
    last = -1 * ((-1 * number) % 10)
print(f"Last digit of {number} is {last} and is " , end = "")
if last > 5:
    print("greater than 5")
elif last == 0:
    print("0")
else:
    print("less than 6 and not 0")
