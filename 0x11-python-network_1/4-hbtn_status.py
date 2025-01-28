#!/usr/bin/python3
"""Fetch url with request"""

import requests

if __name__ == '__main__':

   url = "https://alx-intranet.hbtn.io/status"

   body = requests.get(url)
   print("Body response:")
   print("\t- type:", type(body.text))
   print("\t- content:", body.text)