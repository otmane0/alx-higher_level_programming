#!/bin/bash
#display the length of the conetent
curl -sI $@ | grep -i 'Allow:' | cut -d ' ' -f2- | tr -d '\r'
