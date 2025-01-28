#!/usr/bin/python3
"""fetch specific attr from header of URL"""

from sys import argv
import requests

if __name__ == '__main__':

    url = "http://0.0.0.0:5000/search_user"
    q = argv[1] if len(argv) > 1 else ""

    data = {'q': q}

    try:
        response = requests.post(url, data=data).json()
        if not response:
            print("No result") #empty JSon
        else:
            if "id" in response and "name" in response:
                    print(f"[{response['id']}] {response['name']}")

    except ValueError:
        print("Not a valid JSON")  # Response is not valid JSON



