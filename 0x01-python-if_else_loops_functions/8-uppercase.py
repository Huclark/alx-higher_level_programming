#!/usr/bin/python3

# uppercase - prints a string in uppercase followed by a new line

def uppercase(str):
    output = ""  # declare an empty string

    # loop through string to convert characters to uppercase
    for character in str:
        if 'a' <= character <= 'z':  # check if char falls in lowercase range
            output += chr(ord(character) - 32)  # convert to upper, concatenate
        else:
            output += character  # if uppercase, concatenate

    print(output)
