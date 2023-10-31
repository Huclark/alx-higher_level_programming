#!/usr/bin/python3

for i in range(0, 9):
    for x in range(1, 10):
        if i < x:
            if i == 8:
                print("{:d}{:d}".format(i, x))
            else:
                print("{:d}{:d}, ".format(i, x), end="")
