#!/usr/bin/python3

"""Prints all the names defined by the compiled module hidden_4.pyc"""

if __name__ == "__main__":
    import hidden_4

    names_to_print = dir(hidden_4)

    for name in names_to_print:
        if name[:2] != "__":
            print(name)
