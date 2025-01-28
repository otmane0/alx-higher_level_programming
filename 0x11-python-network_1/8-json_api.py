#!/usr/bin/python3
"""fetch specific attr from header of URL"""

from sys import argv
import requests

if __name__ == '__main__':

    url = "http://0.0.0.0:5000/search_user"
    q = argv[1] if len(argv) > 1 else ""

    data = {'q': q}

    response = requests.post(url, data=data).json()
    try:
        if not response:
            print("No result") #empty JSon
        else:
            if "id" in response and "name" in response:
                    print(f"[{response['id']}] {response['name']}")

    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")  # Response is not valid JSON



