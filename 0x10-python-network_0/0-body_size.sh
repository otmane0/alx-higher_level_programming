#!/bin/bash
#display the length of the conetent
curl -sI $@ -o /dev/null -w '%{size_download}\n'