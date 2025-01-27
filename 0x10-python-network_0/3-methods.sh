#!/bin/bash
#display the length of the conetent
curl -s -X OPTIONS $@ | grep 'Allow:' | cut -d ' ' -f2
