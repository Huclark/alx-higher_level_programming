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
    url = f"{argv[1]}?{urlencode(data).encode('ascii')}"
    
    with urlopen(url) as response:
        print(response.read().decode('utf-8')) 


if __name__ == "__main__":
    post_email()
    
