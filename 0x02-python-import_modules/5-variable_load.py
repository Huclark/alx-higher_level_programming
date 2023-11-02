#!/usr/bin/python3

"""Imports the variable a from the file variable_load_5.py
   and prints its value
"""
if __name__ == "__main__":
    import variable_load_5

    names_defined = dir(variable_load_5)

    if "a" in names_defined:
        a = getattr(variable_load_5, "a")
        print(a)
