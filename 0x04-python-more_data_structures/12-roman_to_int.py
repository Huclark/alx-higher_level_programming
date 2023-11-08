#!/usr/bin/python3
def roman_to_int(roman_string):
    """ Converts a Roman numeral to an integer
    assuming number will be between 1 to 3999.
    """
    if roman_string is None or type(roman_string) is not str:
        return 0

    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    value = roman_numerals[roman_string[len(roman_string) - 1]]

    for i in range(len(roman_string) - 1, 0, -1):
        curr_value = roman_numerals[roman_string[i]]
        prev_value = roman_numerals[roman_string[i - 1]]

        if prev_value >= curr_value:
            value += prev_value
        else:
            value -= prev_value

    return value
