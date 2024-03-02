#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError


def error_code():
    try:
        # make a GET request to the URL
        with urlopen(argv[1]) as response:
            # Read, decode and display the body
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        # Print the error code
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    error_code()
