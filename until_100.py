# infinite.py
# Robert Tate
# 3/15/21
#
# This program demonstrates indefinite iteration by allowing a user
# to enter values until a condition (sum > 100) is met.

sum = 0

while sum <= 100:
    addend = int(input("Please enter a number: "))
    sum += addend
    print(f"Current sum is: {sum}")

print(f"Current sum: {sum} exceeds 100. Program execution complete.")