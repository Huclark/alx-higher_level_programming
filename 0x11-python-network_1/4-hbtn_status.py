#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""
import requests

request = requests.get('https://alx-intranet.hbtn.io/status', timeout=60)

print(
    "Body response:" +
    f"\n\t- type: {type(request.text)}" +
    f"\n\t- content: {request.text}"
)
