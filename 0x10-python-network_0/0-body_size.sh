#!/bin/bash
#Feth size with curl

url=$1
curl -sI $@ | grep 'Content-Length:' | cut -d ' ' -f2