#!/bin/bash
#display the length of the conetent
http_res=$(curl -sI $@ | grep 'HTTP/1.1' | cut -d ' ' -f2); [ "$http_res" == 200 ] && curl -sL $@
