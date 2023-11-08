#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another
    in a new list
    my_list is the initial list
    search is the element to replace in the list
    replace is the new element
    """
 
    new_list = []
    for search_idx in range(len(my_list)):
        if my_list[search_idx] == search:
            new_list.append(replace)
            continue
        new_list.append(my_list[search_idx])
   
    return new_list
