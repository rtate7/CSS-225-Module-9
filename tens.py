# infinite.py
# Robert Tate
# 3/15/21
#
# This program uses a while loop to demonstrate definite iteration.
# The program uses a loop to check if a counter variable is evenly
# divisible by 10 and, if so, adds the current counter value to a
# list. The process is repeated until the counter is greater than 
# 50.

counter = 0
tens = []

while counter <= 50:
    counter += 1
    if counter % 10 == 0: 
        tens.append(counter)

print (tens)