#!/bin/bash
#feth size with curl

url=$1
curl -sI $@ | grep 'Content-Length:' | cut -d ' ' -f2