#!/usr/bin/python3
# This script fetches https://alx-intranet.hbtn.io/status
from urllib.request import Request, urlopen

req = Request('https://alx-intranet.hbtn.io/status')
with urlopen(req) as response:
    the_page = response.read()

obj_type = type(the_page)
print(
    "Body response:" +
    f"\n\t- type: {obj_type}" +
    f"\n\t- content: {the_page}" +
    f"\n\t- utf8 content: {the_page.decode('utf-8')}"
)
