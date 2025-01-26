#!/bin/bash
#display the length of the conetent
curl -s $@ -o /dev/null -w '%{size_download}\n'