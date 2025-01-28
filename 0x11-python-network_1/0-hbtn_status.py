#!/usr/bin/python3
#Fetch URL

url = "https://alx-intranet.hbtn.io/status"

from urllib.request import urlopen

with urlopen(url) as response:
    body = response.read()
print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
print(f"\t- utf8 content: {body.decode('utf-8')}")
