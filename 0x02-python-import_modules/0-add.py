#!/usr/bin/python3

''' This program imports the function def add(a, b): from the file add_0.py
and prints the result of the addition 1 + 2 = 3 '''

from add_0 import add  # import function

# assign values to variables
a = 1
b = 2

''' print result using string format while passing add(a,b) as an
argument to print the result '''

print("{} + {} = {}".format(a, b, add(a, b)))
