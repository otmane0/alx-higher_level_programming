#!/usr/bin/python3
"""manage error exception"""
from sys import argv
from urllib.request import urlopen
from urllib.error import HTTPError

if __name__ == '__main__':
    url = argv[1]
    try:
        with urlopen(url) as response:         # Send the request to the URL and read the response
            body = response.read().decode('utf-8')
            print(body)

    except HTTPError as e:
        print(f"Error code: {e.code}")         # Handle HTTPError and print the error code

