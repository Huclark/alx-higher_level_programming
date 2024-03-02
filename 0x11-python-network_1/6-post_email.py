#!/usr/bin/python3
"""This script takes in a URL and an email,
sends a POST request to the passed URL
with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
from sys import argv
from requests import post


def post_email():
    """Sends a POST request to a URL with the email as a parameter
    and displays the body of the response (decoded in utf-8)
    """
    data = {"email": argv[2]}
    response = post(argv[1], data=data)
    print(response.text)


if __name__ == "__main__":
    post_email()
