#!/usr/bin/python3
"""Get specific key, from a URL header"""
from sys import argv
from urllib.request import urlopen

if __name__ == '__main__':
    url = argv[1]

    with urlopen(url) as response:
        headers = response.info()
        x_request_id = headers.get("X-Request-Id")
    print(x_request_id)
