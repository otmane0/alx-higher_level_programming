#!/usr/bin/python3
"""Post email, new data"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == '__main__':
    url = argv[1]
    email = argv[2]

    data = urlencode({'email': email}).encode('utf-8')     # Prepare the email data as a dictionary

    request = Request(url, data=data)     # Create a POST request

    with urlopen(request) as response:
        body = response.read().decode('utf-8')

    print(body)
