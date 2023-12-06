#!/usr/bin/python3
"""This script retrieves input from the the command line
interface and then saves them as a python list onto a JSON file
"""


if __name__ == "__main__":
    import json
    from sys import argv

    # import relevant modules
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file

    # Open file in append and read mode
    with open("add_item.json", "a+", encoding="utf-8") as file:
        if file.tell() == 0:  # Check if file pointer is at beginning of file
            json.dump([], file)  # Create an empty list

    # Get the current data from JSON file
    file_input = load_from_json_file("add_item.json")

    # Check for valid number of arguments
    if len(argv) > 1:
        file_input.extend(argv[1:])  # Extend list with arguments

    # Save updated list to JSON file
    save_to_json_file(file_input, "add_item.json")
