#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""
import requests

request = requests.get('https://alx-intranet.hbtn.io/status')

obj_type = type(request.text)
print(
    "Body response:" +
    f"\n\t- type: {obj_type}" +
    f"\n\t- content: {request.text}"
)
