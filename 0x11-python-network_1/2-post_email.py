#!/usr/bin/python3
"""This script takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response (decoded in utf-8)
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import urlopen


def post_email():
    data = {}
    data['email'] = argv[2]
    
    # Encode the data to be sent in the request body
    data_encoded = urlencode(data).encode('ascii')

    # Make a POST request to the provided URL with the email parameter
    with urlopen(argv[1], data=data_encoded) as response:
        # read and decode the response body in utf-8
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    post_email()
    
