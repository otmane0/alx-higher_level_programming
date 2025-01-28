#!/usr/bin/python3
"""manage error exception"""

from sys import argv
import requests

if __name__ == '__main__':

    url = argv[1]

    try:
        req = requests.get(url)

        print(req.text)

    except requests.exceptions.HTTPError:
        print(f"Error code: {req.status_code}")         # Handle HTTPError and print the error code

