#!/usr/bin/python3
"""fetch specific attr from header of URL"""

from sys import argv
import requests

if __name__ == '__main__':

    url = "https://api.github.com/user"
    user = argv[1]
    token = argv[2]

    response = requests.get(url, auth=(user, token))
    try:
        data = response.json()
        print(data.get("id"))  # Print 'None' if 'id' is missing
    except ValueError:
        print("None")

