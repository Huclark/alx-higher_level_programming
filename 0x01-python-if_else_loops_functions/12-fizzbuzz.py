#!/usr/bin/python3

# fizzbuzz - prints the numbers from 1 to 100 separated by a space
def fizzbuzz():
    # set loop to iterate from 1 to 100
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:  # if multiple of 3 only
            print("{}".format("Fizz"), end=" ")
        elif i % 5 == 0 and i % 3 != 0:  # if multiple of 5 only
            print("{}".format("Buzz"), end=" ")
        elif i % 3 == 0 and i % 5 == 0:  # if multiple of both 3 and 5
            print("{}".format("FizzBuzz"), end=" ")
        else:
            print("{:d}".format(i), end=" ")
