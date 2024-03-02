#!/usr/bin/python3
# This script takes in a URL, sends a request to the URL and
# displays the value of the X-Request-Id variable found in the header
# of the response.
from urllib.request import Request, urlopen
from sys import argv

req = Request(argv[1])

with urlopen(req) as response:
    print(response.getheader('X-Request-Id'))
