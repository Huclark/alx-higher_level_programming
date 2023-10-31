#!/usr/bin/python3

# islower -  checks for lowercase character
def islower(c):
    # loop through lowercase alphabets (ASCII)
    for i in range(ord('a'), ord('z') + 1):
        if ord(c) == i:  # check if character is lowercase
            return True
    return False
