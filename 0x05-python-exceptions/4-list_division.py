#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.
    If 2 elements can't be divided, the division result
    should be equal to 0

    Args:
        my_list_1: List(integer, string, etc)
        my_list_2: List(integer, string, etc)
        list_length: Size of list

    Return: A new list (length = list_length) with all divisions
    """
    new_list = []
    for idx in range(list_length):
        result = 0
        try:
            result = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list
