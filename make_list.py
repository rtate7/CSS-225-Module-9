# infinite.py
# Robert Tate
# 3/15/21
#
# This program demonstrates definite iteration using a while loop
# by adding a fixed number of elements to a list.

def make_list():
    L = []
    i = 0
    while i <= 10:
        L.append(i)
        i += 1

    return L

print(make_list())