import requests

req = requests.get("http://otmaneks.tech").content
print(req)