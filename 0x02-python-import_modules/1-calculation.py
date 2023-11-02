#!/usr/bin/python3

if __name__ == "__main__":

    '''Prints the results of adding, subtracting, multiplying and
    dividing 10 and 5
    '''
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{} + {} = {}".format(int(a), int(b), add(a, b)))
    print("{} - {} = {}".format(int(a), int(b), sub(a, b)))
    print("{} * {} = {}".format(int(a), int(b), mul(a, b)))
    print("{} / {} = {}".format(int(a), int(b), div(a, b)))
