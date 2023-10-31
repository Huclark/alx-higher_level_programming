#!/usr/bin/python3

# prints the ASCII alphabet, in reverse order, alternating lowercase
# and uppercase (z in lowercase and Y in uppercase), not followed by a new line

for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i - 32)), end="")
