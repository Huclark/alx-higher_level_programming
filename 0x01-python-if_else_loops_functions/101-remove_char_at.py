#!/usr/bin/python3

# remove_char_at - creates a copy of the string and
# removing the character at the position n

def remove_char_at(str, n):
    str_cpy = ""

    for i in range(0, len(str)):
        if i == n:
            continue
        else:
            str_cpy += str[i]

    return str_cpy
