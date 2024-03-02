#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id variable found in the header
of the response."""

from urllib import request
from sys import argv


def x_request_id(args):
    """Sends a request to the URL and displays the value of the
    X-Request-Id variable found in the header of the response

    Args:
        args (str): url
    """
    with request.urlopen(args) as response:
        print(dict(response.headers).get('X-Request-Id'))


if __name__ == "__main__":
    x_request_id(argv[1])
