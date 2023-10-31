#!/usr/bin/python3

# print_last_digit - prints the last digit of a number
def print_last_digit(number):
    print("{}".format(abs(number) % 10), end="")  # print last digit
    return (abs(number) % 10)  # return last digit
