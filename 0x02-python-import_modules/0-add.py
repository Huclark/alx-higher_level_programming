#!/usr/bin/python3

if __name__ == "__main__":
    """Prints the result of the addition 1 and  2"""
    from add_0 import add

    a = 1
    b = 2

    print("{} + {} = {}".format(int(a), int(b), add(a, b)))
