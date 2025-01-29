#!/usr/bin/python3
"""fetch specific attr from header of URL"""

from sys import argv
import requests

if __name__ == '__main__':

    url = "https://api.github.com/user"
    user = argv[1]
    password = argv[2]

    response = requests.get(url, auth=(user, password))
    if response.status_code == 200:
        print(response.json().get("id"))
    else:
        print(f"Error: {response.status_code}")

