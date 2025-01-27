#!/bin/bash
#When you use -d, you are telling the command "here is a specific value or piece of data that I want you to use in this operation.
curl -sI $@ | grep -i 'Allow:' | cut -d ' ' -f2-
