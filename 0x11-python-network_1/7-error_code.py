#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the body of the response.
"""
from sys import argv
from requests import get


def print_body():
    """Prints the body of the http response
    """
    response = get(argv[1], timeout=60)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    print_body()
