#!/bin/bash
#Feth size with curl

url=$1
curl -s "$url" -o /dev/null -w '%{size_download}\n'