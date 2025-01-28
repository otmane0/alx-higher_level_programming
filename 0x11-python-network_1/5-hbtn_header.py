#!/usr/bin/python3
"""fetch specific attr from header of URL"""

from sys import argv
import requests

if __name__ == '__main__':

    url = argv[1]
    req = requests.get(url)
    x_request_id = req.headers.get("X-Request-Id")
    print(x_request_id)

