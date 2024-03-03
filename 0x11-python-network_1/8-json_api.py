#!/usr/bin/python3
"""This script takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
from sys import argv
from requests import post


def json_api():
    """This method takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
    """
    # construct the dictionary
    data = {"q": argv[1] if len(argv) > 1 else ""}
    # get the http response
    url = "http://0.0.0.0:5000/search_user"
    response = post(url, data=data, timeout=60)

    try:
        result = response.json()
        if result:
            print(f"[{result.get('id')}] {result.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    json_api()
