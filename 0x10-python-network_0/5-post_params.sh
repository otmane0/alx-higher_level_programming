#!/bin/bash
#"key1=value1&key2=value2&key3=value3&..."
curl -s -X POST $@ -d "email=test@gmail.com&subject=I will always be here for PLD" 
