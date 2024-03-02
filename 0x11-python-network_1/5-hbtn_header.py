#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the
response header
"""
from sys import argv
from requests import get


def x_request_id():
    """Sends a request to a url and displays the value of the
    variable X-Rquest-Id in the response header
    """
    response = get(argv[1])
    print(response.headers['X-Request-Id'])


if __name__ == "__main__":
    x_request_id()
