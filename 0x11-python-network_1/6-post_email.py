#!/usr/bin/python3
"""fetch specific attr from header of URL"""

from sys import argv
import requests

if __name__ == '__main__':

    url = argv[1]
    email = argv[2]
    data = {'email': email}


    response = requests.post(url, data=data)
    print(response.content)

