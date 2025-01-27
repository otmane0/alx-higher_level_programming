#!/bin/bash
#display the length of the conetent
curl -s -X OPTIONS $@ | grep -i 'Allow:' | cut -d ' ' -f2- | tr -d '\r'
